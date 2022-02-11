from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from morse_coder import MorseCoder

app = Flask(__name__)
app.config["SECRET_KEY"] = "this is a temporary key"
Bootstrap(app)
coder = MorseCoder()


class InputForm(FlaskForm):
    user_input = TextAreaField()
    encode = SubmitField("Encode")
    undo = SubmitField("Undo")
    decode = SubmitField("Decode")


@app.route("/", methods=["GET", "POST"])
def home():
    form = InputForm()
    if form.validate_on_submit():
        text = form.user_input.data
        morse_code = coder.encode(text)
        print(morse_code)

        return render_template("index.html", form=form, morse_code=morse_code)

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
