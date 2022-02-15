from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from morse_coder import MorseCoder

app = Flask(__name__)
app.config["SECRET_KEY"] = "this is a temporary key"
Bootstrap(app)
coder = MorseCoder()

session_history = []


@app.route("/", methods=["GET"])
def home():

    text_fill = request.args.get("text_fill")

    return render_template("index.html", text_fill=text_fill)


@app.route("/encode", methods=["POST"])
def encode():

    if request.method == "POST":
        text = request.form["user-input"]

        if text:
            session_history.append(text)

        morse_code = coder.encode(text)

        return redirect(url_for("home", text_fill=morse_code))


@app.route("/decode", methods=["POST"])
def decode():

    if request.method == "POST":
        morse_code = request.form["user-input"]

        if morse_code:
            session_history.append(morse_code)

        text = coder.decode(morse_code)

        return redirect(url_for("home", text_fill=text))


@app.route("/clear", methods=["POST"])
def clear():
    if request.method == "POST":
        return redirect(url_for("home"))


@app.route("/undo", methods=["GET", "POST"])
def undo():
    if session_history:
        text = session_history.pop()
    else:
        text = None

    return redirect(url_for("home", text_fill=text))


if __name__ == "__main__":
    app.run(debug=True)
