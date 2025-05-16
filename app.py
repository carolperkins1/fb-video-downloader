
from flask import Flask, render_template, request
import yt_dlp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    video_data = None
    error = None

    if request.method == 'POST':
        fb_url = request.form['videoURL']
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'skip_download': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(fb_url, download=False)
                video_data = {
                    'title': info_dict.get('title'),
                    'formats': [
                        {
                            'url': fmt.get('url'),
                            'format': fmt.get('format_note') or fmt.get('ext'),
                            'resolution': fmt.get('height') or 'audio'
                        }
                        for fmt in info_dict.get('formats', [])
                        if fmt.get('url')
                    ]
                }

        except Exception as e:
            error = f"Failed to extract video: {str(e)}"

    return render_template('index.html', video_data=video_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
