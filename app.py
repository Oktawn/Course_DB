from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField


class RestrForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField()


# class SingUpForm(FlaskForm):
#     username = StringField("Username")
#     password = PasswordField("Password")
#     submit = SubmitField()


app = Flask(__name__)
app.config["SECRET_KEY"] = "the random string"


@app.route("/home", methods=["GET", "POST"])
def home(username):
    return render_template("home.html", user=username)


@app.route("/singup", methods=["GET", "POST"])
def singup():
    form = RestrForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return home(username)
    return render_template("singup.html", form=form)


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    form = RestrForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return home(username)
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    return login()


if __name__ == "__main__":
    app.run(debug=True)
