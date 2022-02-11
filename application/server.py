from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from morse_coder import MorseCoder

app = Flask(__name__)
Bootstrap(app)
coder = MorseCoder()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["user_text"]
        morse_code = coder.encode(text)

        return render_template("index.html", morse_code=morse_code)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
