from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from morse_coder import MorseCoder

app = Flask(__name__)
app.config["SECRET_KEY"] = "this is a temporary key"
Bootstrap(app)
coder = MorseCoder()


@app.route("/", methods=["GET"])
def home():

    try:
        text_fill = session["history"].pop()
        session.modified = True

    except KeyError:
        session["history"] = []
        text_fill = None

    except IndexError:
        text_fill = None

    return render_template("index.html", text_fill=text_fill)


@app.route("/encode", methods=["POST"])
def encode():

    if request.method == "POST":
        text = request.form["user-input"]

        if text:
            morse_code = coder.encode(text)
            session["history"].extend([text, morse_code])
            session.modified = True

        return redirect(url_for("home"))


@app.route("/decode", methods=["POST"])
def decode():

    if request.method == "POST":
        morse_code = request.form["user-input"]

        if morse_code:
            text = coder.decode(morse_code)
            session["history"].extend([morse_code, text])
            session.modified = True

        return redirect(url_for("home"))


@app.route("/clear", methods=["GET"])
def clear():

    session["history"].append("")
    session.modified = True
    return redirect(url_for("home"))


@app.route("/undo", methods=["GET"])
def undo():

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
