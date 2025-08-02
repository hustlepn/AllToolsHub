from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tools/downloader')
def downloader():
    return render_template('tools/downloader.html')

@app.route('/tools/urlshortener')
def urlshortener():
    return render_template('tools/urlshortener.html')

@app.route('/tools/calculators')
def calculators():
    return render_template('tools/calculators.html')

@app.route('/tools/pdf')
def pdf_tools():
    return render_template('tools/pdf.html')

@app.route('/tools/qr')
def qr_generator():
    return render_template('tools/qr.html')

@app.route('/blog')
def blog():
    return render_template('blog/index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

if __name__ == '__main__':
    app.run(debug=True)
