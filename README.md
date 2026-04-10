# Romantic Surprise Web Application 💕

A beautiful Flask web application that allows users to create personalized romantic surprise webpages with photos, messages, and background music.

## Features

- **Beautiful Home Page**: Romantic pink design with call-to-action
- **Form Page**: User-friendly form to create surprises
  - Name inputs for both partners
  - Custom romantic message
  - Upload up to 3 images
  - Choose background music (3 options)
- **Surprise Page**: Generated romantic webpage with
  - Personalized message with names
  - Image carousel with animations
  - Background music autoplay
  - WhatsApp share functionality
  - Mobile-responsive design
- **Storage**: Local JSON storage and image uploads
- **Animations**: Floating hearts, fade-in effects, smooth transitions

## Project Structure

```
romantic-surprise/
├── app.py                 # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── templates/             # HTML templates
│   ├── index.html         # Home page
│   ├── create.html        # Form page
│   ├── surprise.html      # Generated surprise page
│   └── 404.html           # 404 error page
├── static/                # Static files
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   ├── js/                # JavaScript files (if needed)
│   ├── music/             # Background music files
│   │   └── README.txt     # Music file instructions
│   └── images/            # Static images
├── uploads/               # User uploaded images
└── data/                  # JSON data storage
    └── surprises.json     # Surprise data
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or download the project** to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd romantic-surprise
   ```

3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Add background music files** (optional):
   - Download 3 romantic MP3 files
   - Place them in `static/music/` with these exact names:
     - `romantic1.mp3` - Romantic piano music
     - `romantic2.mp3` - Sweet melody  
     - `romantic3.mp3` - Love symphony
   
   You can find royalty-free music from:
   - YouTube Audio Library
   - Pixabay Music
   - Freesound.org

## Running the Application

1. **Start the Flask application**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and go to:
   ```
   http://localhost:5000
   ```

3. **The application is now running!** You can:
   - Visit the home page
   - Create romantic surprises
   - Share generated links

## Usage

### Creating a Surprise

1. Click "Create Your Surprise" on the home page
2. Fill in the form:
   - Your name
   - Partner's name
   - Romantic message
   - Upload up to 3 images (PNG, JPG, JPEG, GIF, WebP)
   - Choose background music
3. Click "Create Surprise"
4. You'll be redirected to a unique URL with your surprise page

### Sharing

- Use the WhatsApp share button to send directly
- Copy the link to share anywhere
- The link is permanent and can be accessed anytime

## Features Details

### Design
- **Color Scheme**: Pink gradient background with romantic aesthetics
- **Typography**: Georgia serif with Dancing Script for headings
- **Responsive**: Works perfectly on mobile, tablet, and desktop
- **Animations**: Floating hearts, fade-in effects, smooth transitions

### Technical Features
- **File Upload**: Secure image upload with validation
- **Data Storage**: JSON-based storage for simplicity
- **URL Generation**: Unique IDs for each surprise
- **Error Handling**: 404 page for invalid URLs
- **Form Validation**: Client and server-side validation

### Browser Compatibility
- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## Troubleshooting

### Common Issues

1. **Port 5000 already in use**:
   ```bash
   # Kill existing process or use different port
   python app.py --port 5001
   ```

2. **Music not playing**:
   - Modern browsers block autoplay
   - Music will play after first user interaction
   - Check browser console for errors

3. **Images not uploading**:
   - Check file size (max 16MB per file)
   - Ensure file format is supported
   - Check uploads folder permissions

4. **Template errors**:
   - Ensure all template files are in the `templates/` folder
   - Check Jinja2 syntax

### Development Tips

- **Debug mode**: The app runs in debug mode by default
- **Logs**: Check terminal for error messages
- **Storage**: All data is stored locally in `data/surprises.json`
- **Images**: Uploaded images are stored in `uploads/` folder

## Customization

### Adding New Music
1. Place MP3 files in `static/music/`
2. Update the music options in `templates/create.html`
3. Update the music filename mapping in `app.py`

### Changing Colors
Edit `static/css/style.css`:
- Change gradient colors in `body` selector
- Update button colors in `.btn` class
- Modify form colors in `.form-control` class

### Adding New Features
- Add new routes in `app.py`
- Create new templates in `templates/`
- Add new styles in `static/css/style.css`

## Security Notes

- **File Upload**: Only image files are allowed
- **File Size**: Limited to 16MB per file
- **Input Validation**: All user inputs are validated
- **XSS Protection**: Jinja2 auto-escapes content

## Deployment

### For Production Use

1. **Disable debug mode**:
   ```python
   app.run(debug=False, host='0.0.0.0', port=5000)
   ```

2. **Use a production server**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Set up reverse proxy** (nginx/Apache)

4. **Configure HTTPS** for secure connections

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the error logs in the terminal
3. Ensure all dependencies are properly installed

## Enjoy! 💕

Create beautiful romantic surprises and make someone's day special!
