from flask import Flask, render_template, request, redirect, url_for, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)

DOWNLOAD_FOLDER = 'downloads'
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('tools/video-downloader.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    uid = str(uuid.uuid4())
    output_path = f"{DOWNLOAD_FOLDER}/{uid}.mp4"

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': output_path,
        'quiet': True,
        'noplaylist': True
    }

    info = None
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        return render_template('tools/video-downloader.html', 
                               success=True,
                               title=info.get('title'),
                               thumbnail=info.get('thumbnail'),
                               duration=info.get('duration'),
                               filename=os.path.basename(output_path))
    except Exception as e:
        return render_template('tools/video-downloader.html', error=str(e))

@app.route('/download_file/<filename>')
def download_file(filename):
    return send_file(os.path.join(DOWNLOAD_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
