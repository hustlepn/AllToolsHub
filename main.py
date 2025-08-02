from flask import Flask, render_template, request, redirect, url_for
import yt_dlp
import secrets
import string
from urllib.parse import urlparse

app = Flask(__name__)

# In-memory storage for URL shortener
url_mapping = {}

# Helper function for URL shortener
def generate_short_code():
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(6))

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

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

# Essential Pages
@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/privacy')
def privacy():
    return render_template('pages/privacy.html')

@app.route('/terms')
def terms():
    return render_template('pages/terms.html')

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

@app.route('/blog/url-shortener-guide')
def url_shortener_guide():
    return render_template('blog/url-shortener-guide.html')

@app.route('/blog/pdf-tools-guide')
def pdf_tools_guide():
    return render_template('blog/pdf-tools-guide.html')

@app.route('/blog/calculator-tips')
def calculator_tips():
    return render_template('blog/calculator-tips.html')

@app.route('/blog/qr-code-uses')
def qr_code_uses():
    return render_template('blog/qr-code-uses.html')

@app.route('/blog/video-downloader-faq')
def video_downloader_faq():
    return render_template('blog/video-downloader-faq.html')

@app.route('/blog/url-safety-guide')
def url_safety_guide():
    return render_template('blog/url-safety-guide.html')

@app.route('/blog/pdf-security')
def pdf_security():
    return render_template('blog/pdf-security.html')

@app.route('/blog/mobile-optimization')
def mobile_optimization():
    return render_template('blog/mobile-optimization.html')

@app.route('/blog/tools-update')
def tools_update():
    return render_template('blog/tools-update.html')

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
