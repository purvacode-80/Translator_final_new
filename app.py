from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    source_lang = request.form['source_lang']
    dest_langs = request.form.getlist('dest_lang[]')
    text = request.form['text']
    translator = Translator()
    translations = {}

    for lang in dest_langs:
        translated = translator.translate(text, src=source_lang, dest=lang)
        translations[lang] = translated.text

    formatted_translations = "\n".join([f"{lang}: {text}" for lang, text in translations.items()])
    
    return render_template('index.html', translations=formatted_translations)