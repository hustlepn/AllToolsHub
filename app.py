from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/video-guide')
def blog_video_guide():
    return render_template('blog_posts/video_guide.html')

@app.route('/blog/url-safety')
def blog_url_safety():
    return render_template('blog_posts/url_safety.html')

@app.route('/blog/pdf-security')
def blog_pdf_security():
    return render_template('blog_posts/pdf_security.html')

@app.route('/tools/downloader')
def tool_downloader():
    return render_template('tools/downloader.html')

@app.route('/tools/shortener')
def tool_shortener():
    return render_template('tools/shortener.html')

@app.route('/tools/qr')
def tool_qr():
    return render_template('tools/qr.html')

@app.route('/tools/pdf-tools')
def tool_pdf():
    return render_template('tools/pdf_tools.html')

@app.route('/tools/calculator')
def tool_calculator():
    return render_template('tools/calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
