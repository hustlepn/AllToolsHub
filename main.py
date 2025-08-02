from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/downloader')
def downloader():
    return render_template('tools/downloader.html')

@app.route('/urlshortener')
def url_shortener():
    return render_template('tools/urlshortener.html')

@app.route('/calculators')
def calculators():
    return render_template('tools/calculators.html')

@app.route('/pdf')
def pdf_tools():
    return render_template('tools/pdftools.html')

@app.route('/qrcode')
def qr_generator():
    return render_template('tools/qrcode.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
