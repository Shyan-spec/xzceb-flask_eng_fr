import machinetranslation 

from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get(englishToFrench)

    return textToTranslate

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get(frenchToEnglish)
    return textToTranslate

@app.route("/index.html")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
