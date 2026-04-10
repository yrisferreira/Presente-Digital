from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import uuid
import json
from datetime import datetime, timedelta
import secrets
import stripe
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuração
app.secret_key = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

# Configuração Email
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER', '')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD', '')

# Configuração Stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY', '')

# Inicialização
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'
mail = Mail(app)

# Criar pastas
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('static/music', exist_ok=True)

# Modelos de Dados
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    plano = db.Column(db.String(20), default='gratuito')  # gratuito, basico, premium, ilimitado
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    creditos = db.Column(db.Integer, default=1)  # Créditos para criar surpresas
    stripe_customer_id = db.Column(db.String(100))
    
    surprises = db.relationship('Surprise', backref='autor', lazy=True)
    pagamentos = db.relationship('Pagamento', backref='usuario', lazy=True)

class Surprise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_unico = db.Column(db.String(20), unique=True, nullable=False)
    seu_nome = db.Column(db.String(100), nullable=False)
    nome_parceiro = db.Column(db.String(100), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    musica = db.Column(db.String(50), default='romantic1')
    imagens = db.Column(db.Text)  # JSON com nomes dos arquivos
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), default='ativo')  # ativo, inativo, expirado

class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    stripe_payment_id = db.Column(db.String(100))
    valor = db.Column(db.Float, nullable=False)
    plano = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='pendente')  # pendente, aprovado, cancelado
    data_pagamento = db.Column(db.DateTime, default=datetime.utcnow)

# Configuração Login Manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Funções auxiliares
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# Rotas Principais
@app.route('/')
def index():
    return render_template('index_meupresente.html')

@app.route('/planos')
def planos():
    return render_template('planos_v2.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Nome de usuário já existe!')
            return redirect(url_for('cadastro'))
        
        if User.query.filter_by(email=email).first():
            flash('Email já cadastrado!')
            return redirect(url_for('cadastro'))
        
        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        
        db.session.add(user)
        db.session.commit()
        
        flash('Cadastro realizado com sucesso! Faça login para continuar.')
        return redirect(url_for('login'))
    
    return render_template('auth/cadastro_v3.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_or_email = request.form.get('username')
        password = request.form.get('password')
        
        # Tentar encontrar por username ou email
        user = User.query.filter(
            (User.username == username_or_email) | (User.email == username_or_email)
        ).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash(f'Bem-vindo de volta, {user.username}!')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Email/Usuário ou senha incorretos!')
    
    return render_template('auth/login_v3.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    surprises = Surprise.query.filter_by(usuario_id=current_user.id).order_by(Surprise.data_criacao.desc()).all()
    return render_template('dashboard.html', surprises=surprises)

@app.route('/criar', methods=['GET', 'POST'])
@login_required
def criar_surpresa():
    if current_user.creditos <= 0:
        flash('Você não tem créditos suficientes! Adquira um plano para continuar.')
        return redirect(url_for('planos'))
    
    if request.method == 'POST':
        try:
            # Obter dados do formulário
            seu_nome = request.form.get('seu_nome', '').strip()
            nome_parceiro = request.form.get('nome_parceiro', '').strip()
            mensagem = request.form.get('mensagem', '').strip()
            musica = request.form.get('musica', 'romantic1')
            
            # Validação
            if not seu_nome or not nome_parceiro or not mensagem:
                flash('Por favor, preencha todos os campos obrigatórios!')
                return redirect(url_for('criar_surpresa'))
            
            # Processar uploads de imagens
            imagens_uploads = []
            files = request.files.getlist('imagens')
            
            for file in files:
                if file and file.filename != '':
                    filename = secure_filename(file.filename)
                    if filename and '.' in filename and filename.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg', 'gif', 'webp']:
                        unique_filename = f"{uuid.uuid4()}_{filename}"
                        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                        file.save(file_path)
                        imagens_uploads.append(unique_filename)
            
            # Gerar ID único
            id_unico = str(uuid.uuid4())[:8]
            
            # Criar surpresa
            surpresa = Surprise(
                id_unico=id_unico,
                seu_nome=seu_nome,
                nome_parceiro=nome_parceiro,
                mensagem=mensagem,
                musica=musica,
                imagens=json.dumps(imagens_uploads),
                usuario_id=current_user.id
            )
            
            # Deduzir crédito
            current_user.creditos -= 1
            
            db.session.add(surpresa)
            db.session.commit()
            
            flash('Surpresa criada com sucesso!')
            return redirect(url_for('visualizar_surpresa', id_unico=id_unico))
            
        except Exception as e:
            print(f"Erro: {e}")
            flash('Ocorreu um erro ao criar sua surpresa. Tente novamente.')
            return redirect(url_for('criar_surpresa'))
    
    return render_template('criar_meupresente.html')

@app.route('/surpresa/<id_unico>')
def visualizar_surpresa(id_unico):
    surpresa = Surprise.query.filter_by(id_unico=id_unico, status='ativo').first()
    
    if not surpresa:
        return render_template('404.html'), 404
    
    # Converter imagens de JSON para lista
    if surpresa.imagens:
        try:
            surpresa.imagens_lista = json.loads(surpresa.imagens)
        except:
            surpresa.imagens_lista = []
    else:
        surpresa.imagens_lista = []
    
    return render_template('surpresa_meupresente.html', surpresa=surpresa)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/static/music/<filename>')
def music_file(filename):
    return send_from_directory('static/music', filename)

# Rotas de Pagamento
@app.route('/pagamento/<plano>')
@login_required
def pagamento(plano):
    planos_disponiveis = {
        'eterno': {'nome': 'Plano Eterno', 'preco': 29.90, 'creditos': 1, 'descricao': 'Sua surpresa online para sempre'},
        'ilimitado': {'nome': 'Plano Ilimitado', 'preco': 79.90, 'creditos': 999, 'descricao': 'Surpresas ilimitadas por 30 dias'},
        'basico': {'nome': 'Plano Básico', 'preco': 19.90, 'creditos': 5, 'descricao': '5 surpresas românticas'},
        'premium': {'nome': 'Plano Premium', 'preco': 39.90, 'creditos': 15, 'descricao': '15 surpresas + recursos exclusivos'}
    }
    
    if plano not in planos_disponiveis:
        flash('Plano inválido!')
        return redirect(url_for('planos'))
    
    plano_info = planos_disponiveis[plano]
    
    # Criar sessão de pagamento Stripe
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'brl',
                    'product_data': {
                        'name': plano_info['nome'],
                        'description': plano_info['descricao'],
                    },
                    'unit_amount': int(plano_info['preco'] * 100),  # Converter para centavos
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=url_for('pagamento_sucesso', plano=plano, _external=True),
            cancel_url=url_for('pagamento_cancelado', _external=True),
            customer_email=current_user.email,
        )
        
        return redirect(checkout_session.url)
        
    except Exception as e:
        print(f"Erro Stripe: {e}")
        flash('Erro ao processar pagamento. Tente novamente.')
        return redirect(url_for('planos'))

@app.route('/pagamento/sucesso/<plano>')
@login_required
def pagamento_sucesso(plano):
    planos_disponiveis = {
        'eterno': {'creditos': 1, 'plano_nome': 'eterno'},
        'ilimitado': {'creditos': 999, 'plano_nome': 'ilimitado'},
        'basico': {'creditos': 5, 'plano_nome': 'basico'},
        'premium': {'creditos': 15, 'plano_nome': 'premium'}
    }
    
    if plano in planos_disponiveis:
        plano_info = planos_disponiveis[plano]
        
        # Atualizar créditos do usuário
        current_user.creditos += plano_info['creditos']
        current_user.plano = plano_info['plano_nome']
        
        # Registrar pagamento
        pagamento = Pagamento(
            usuario_id=current_user.id,
            plano=plano_info['plano_nome'],
            valor={'eterno': 29.90, 'ilimitado': 79.90, 'basico': 19.90, 'premium': 39.90}[plano],
            status='aprovado'
        )
        
        db.session.add(pagamento)
        db.session.commit()
        
        flash(f'Pagamento realizado com sucesso! Você agora tem {current_user.creditos} créditos.')
    
    return redirect(url_for('dashboard'))

@app.route('/pagamento/cancelado')
def pagamento_cancelado():
    flash('Pagamento cancelado. Você pode tentar novamente quando quiser.')
    return redirect(url_for('planos'))

# Webhook Stripe
@app.route('/webhook/stripe', methods=['POST'])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('stripe-signature')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, os.getenv('STRIPE_WEBHOOK_SECRET', '')
        )
    except ValueError as e:
        return 'Invalid payload', 400
    except stripe.error.SignatureVerificationError as e:
        return 'Invalid signature', 400
    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(f"Pagamento confirmado: {session}")
    
    return 'Success', 200

# Rota Admin
@app.route('/admin')
@login_required
def admin():
    if current_user.username != 'admin':
        flash('Acesso negado!')
        return redirect(url_for('dashboard'))
    
    usuarios = User.query.all()
    surpresas = Surprise.query.all()
    pagamentos = Pagamento.query.all()
    
    return render_template('admin/dashboard.html', usuarios=usuarios, surpresas=surpresas, pagamentos=pagamentos)

# Rota 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True, host='0.0.0.0', port=5004)
