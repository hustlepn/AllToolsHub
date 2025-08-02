from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import yt_dlp
import secrets
import string
from urllib.parse import urlparse
from datetime import datetime

app = Flask(__name__)

# In-memory storage for URL shortener
url_mapping = {}

# Helper function for URL shortener
def generate_short_code():
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(6))

# Google Verification (replace with your actual filename)
@app.route('/google1234567890.html')  # ← CHANGE THIS TO YOUR FILE
def google_verification():
    return send_from_directory('static', 'google1234567890.html')  # ← AND THIS

# Dynamic Sitemap
@app.route('/sitemap.xml')
def sitemap():
    base_url = request.host_url.rstrip('/')
    urls = [
        {
            'loc': f"{base_url}/",
            'lastmod': datetime.now().strftime('%Y-%m-%d'),
            'priority': '1.0'
        },
        # Add all other URLs in this format:
        {
            'loc': f"{base_url}/downloader",
            'lastmod': datetime.now().strftime('%Y-%m-%d'),
            'priority': '0.8'
        },
        # Include all your tools, pages, and blog posts
    ]
    response = render_template('sitemap.xml', urls=urls)
    response.headers['Content-Type'] = 'application/xml'
    return response

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Robots.txt
@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

# Tool Pages
@app.route('/downloader')
def downloader():
    return render_template('tools/downloader.html')

@app.route('/urlshortener', methods=['GET', 'POST'])
def url_shortener():
    short_url = None
    if request.method == 'POST':
        long_url = request.form['long_url']
        parsed = urlparse(long_url)
        if not all([parsed.scheme, parsed.netloc]):
            return render_template('tools/urlshortener.html', error="Invalid URL format")
        short_code = generate_short_code()
        url_mapping[short_code] = long_url
        short_url = f"{request.host_url}{short_code}"
    return render_template('tools/urlshortener.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_short_url(short_code):
    if short_code in url_mapping:
        return redirect(url_mapping[short_code])
    return render_template('pages/404.html'), 404

@app.route('/calculators')
def calculators():
    return render_template('tools/calculators.html')

@app.route('/pdf')
def pdf_tools():
    return render_template('tools/pdftools.html')

@app.route('/qrcode')
def qr_generator():
    return render_template('tools/qrcode.html')

# Essential Pages (reorganized)
@app.route('/privacy')
def privacy():
    return render_template('pages/privacy.html')

@app.route('/terms')
def terms():
    return render_template('pages/terms.html')

@app.route('/about')  # Moved next to terms/privacy
def about():
    return render_template('pages/about.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

# Blog Pages
@app.route('/blog')
def blog_home():
    return render_template('blog/index.html')

@app.route('/blog/how-to-use-video-downloader')
def video_downloader_guide():
    return render_template('blog/how-to-use-video-downloader.html')

# [Keep all other existing blog routes...]

# Video Downloader API
@app.route('/download', methods=['POST'])
def download_video():
    url = request.form.get('url')
    if not url:
        return {"error": "URL is required"}, 400
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get('title'),
                "thumbnail": info.get('thumbnail'),
                "formats": info.get('formats'),
            }
    except Exception as e:
        return {"error": str(e)}, 500

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('pages/500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
