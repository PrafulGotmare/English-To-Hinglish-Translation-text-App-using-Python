from flask import Flask, render_template, request
from mtranslate import translate

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    hinglish_translation = ""

    if request.method == 'POST':
        input_text = request.form['input_text']
        hinglish_translation = translate(input_text, to_language='hi', from_language='en')

    return render_template('index.html', hinglish_translation=hinglish_translation)

if __name__ == '__main__':
    app.run(debug=True)
