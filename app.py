from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from check_db import create_user, check_user
from werkzeug.security import generate_password_hash

class RestrForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField()


class SingUpForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField()


app = Flask(__name__)
app.config["SECRET_KEY"] = "the random string"


@app.route("/home", methods=["GET", "POST"])
def home(username):
    return render_template("home.html", user=username)


# @app.route("/singup", methods=["GET", "POST"])
# def singup():
#     form = SingUpForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data
#         hash_password = generate_password_hash(str(password))
#         create_user(username, hash_password)
#         return login()
#     return render_template("singup.html", form=form)

@app.route("/error")
def error(name_error):
    return render_template("error.html", name_error = name_error)


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    form = RestrForm()
    username = form.username.data 
    password = form.password.data
    if form.validate_on_submit():
        if check_user(username, password) == True:
            return home(username)
        else:
            return error(name_error="Данного пользователя не существует")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    return login()


if __name__ == "__main__":
    app.run(debug=True)
