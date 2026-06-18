from flask import Flask, render_template, request, send_file
from deep_translator import GoogleTranslator
from gtts import gTTS

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    translated_text = ""
    input_text = ""

    if request.method == "POST":

        text = request.form["text"]
        input_text = text
        source = request.form["source"]
        target = request.form["target"]

        translated_text = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

    return render_template(
        "index.html",
        translated_text=translated_text,
        input_text=input_text
    )

@app.route("/speak/<lang>/<path:text>")
def speak(lang, text):

    tts = gTTS(text=text, lang=lang)
    tts.save("speech.mp3")

    return send_file(
        "speech.mp3",
        mimetype="audio/mpeg"
    )

if __name__ == "__main__":
    app.run(debug=True)