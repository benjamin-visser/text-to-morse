import numpy as np
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from scipy.io.wavfile import write

import morse_coder

app = Flask(__name__)
app.config["SECRET_KEY"] = "this is a temporary key"
Bootstrap(app)


@app.route("/", methods=["GET"])
def home():

    try:
        text_fill = session["history"][-1]
        # print("Session history @home:", session["history"])
        # print("Text fill:", text_fill)

    except KeyError:
        session["history"] = []
        text_fill = None

    except IndexError:
        text_fill = None

    try:
        audio_enabled = session["audio_enabled"]
    except KeyError:
        session["audio_enabled"] = False
        audio_enabled = False

    return render_template("index.html", text_fill=text_fill, audio_enabled=audio_enabled)


@app.route("/encode", methods=["POST"])
def encode():

    text = request.form["user-input"]

    if text:
        morse_code = morse_coder.encode(text)
        session["history"].append({"type": "morse", "content": morse_code})
        session["audio_enabled"] = False
        session.modified = True
        # print("Session history after encode:", session["history"])

    return redirect(url_for("home"))


@app.route("/decode", methods=["POST"])
def decode():

    morse_code = request.form["user-input"]

    if morse_code:
        text = morse_coder.decode(morse_code)
        session["history"].append({"type": "text", "content": text})
        session["audio_enabled"] = False
        session.modified = True
        # print("Session history after decode:", session["history"])

    return redirect(url_for("home"))


@app.route("/clear")
def clear():

    session["history"].append("")
    session["audio_enabled"] = False
    session.modified = True

    return redirect(url_for("home"))


@app.route("/undo")
def undo():

    if session["history"]:
        session["history"].pop()
        session["audio_enabled"] = False
        session.modified = True

    return redirect(url_for("home"))


@app.route("/play-audio", methods=["GET"])
def get_audio():

    morse_string = session["history"][-1]["content"]

    # print("Morse string to write:", morse_string)

    audio_signal, sample_rate = morse_coder.generate_audio(morse_string)

    write("static/audio/example.wav", sample_rate, audio_signal.astype(np.int16))
    # print("writing file... hopefully")

    session["audio_enabled"] = True
    session.modified = True

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
