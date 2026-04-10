from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
import os
import uuid
import json
from datetime import datetime
import secrets
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('data', exist_ok=True)

# Data storage file
DATA_FILE = 'data/surprises.json'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_surprises():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    except:
        return {}

def save_surprises(surprises):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(surprises, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        your_name = request.form.get('your_name', '').strip()
        partner_name = request.form.get('partner_name', '').strip()
        message = request.form.get('message', '').strip()
        music_choice = request.form.get('music', 'romantic1')
        
        # Validation
        if not your_name or not partner_name or not message:
            flash('Please fill in all required fields!')
            return redirect(url_for('create'))
        
        # Handle file uploads
        uploaded_files = []
        files = request.files.getlist('images')
        
        for file in files:
            if file and file.filename != '':
                if allowed_file(file.filename):
                    # Generate unique filename
                    filename = secure_filename(file.filename)
                    unique_filename = f"{uuid.uuid4()}_{filename}"
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                    file.save(file_path)
                    uploaded_files.append(unique_filename)
                else:
                    flash('Invalid file type! Please upload images only.')
                    return redirect(url_for('create'))
        
        # Generate unique ID
        surprise_id = str(uuid.uuid4())[:8]
        
        # Create surprise data
        surprise_data = {
            'id': surprise_id,
            'your_name': your_name,
            'partner_name': partner_name,
            'message': message,
            'music': music_choice,
            'images': uploaded_files,
            'created_at': datetime.now().isoformat()
        }
        
        # Save to storage
        surprises = load_surprises()
        surprises[surprise_id] = surprise_data
        save_surprises(surprises)
        
        return redirect(url_for('surprise', id=surprise_id))
        
    except Exception as e:
        print(f"Error: {e}")
        flash('An error occurred while creating your surprise. Please try again.')
        return redirect(url_for('create'))

@app.route('/surprise/<id>')
def surprise(id):
    surprises = load_surprises()
    surprise_data = surprises.get(id)
    
    if not surprise_data:
        return render_template('404.html'), 404
    
    return render_template('surprise.html', surprise=surprise_data)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/static/music/<filename>')
def music_file(filename):
    return send_from_directory('static/music', filename)

@app.errorhandler(413)
def too_large(e):
    flash('File too large! Please upload images smaller than 16MB.')
    return redirect(url_for('create'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
