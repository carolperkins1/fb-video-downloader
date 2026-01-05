
from flask import Flask, render_template, request

app = Flask(__name__)


STYLE_GUIDE = (
    "abandoned theme-park animatronic scene, life-sized sculptural figure, "
    "dusty decayed interior, heavy cobwebs, broken furniture, low moody lighting, "
    "uncanny nostalgic tone, stillness, cinematic realism, highly detailed textures"
)

VARIATIONS = [
    "sleeping pose at a worn table, soft rim light, shallow depth of field",
    "chained on a cold concrete floor, harsh overhead spotlight, wide angle",
    "slumped in a wooden chair, diffused window light, medium shot",
    "collapsed beside a cracked prop set, foggy haze, low angle",
    "upright but lifeless in a dusty corner, flashlight beam, close-up detail",
]


def build_prompts(subject):
    prompts = []
    for variation in VARIATIONS:
        prompts.append(
            f"{subject}, {variation}, {STYLE_GUIDE}"
        )
    return prompts


@app.route('/', methods=['GET', 'POST'])
def index():
    prompts = None
    error = None
    subject = ""

    if request.method == 'POST':
        subject = request.form.get('subject', '').strip()
        if subject:
            prompts = build_prompts(subject)
        else:
            error = "Please enter a character, movie, cartoon, or game."

    return render_template(
        'index.html',
        prompts=prompts,
        error=error,
        subject=subject
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
