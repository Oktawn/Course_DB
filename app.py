from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from check_db import create_user, check_user, get_data_user
from werkzeug.security import generate_password_hash

class RestrForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField()


app = Flask(__name__)
app.config["SECRET_KEY"] = "the random string"


@app.route("/home", methods=["GET", "POST"])
def home(username):
    student = get_data_user(username)
    group_id = str(student[-6:-2])
    return render_template("new_home.html", user=username, group = group_id)


@app.route('/schedule/<group>', methods=["GET", "POST"])
def schedule(group):
    iframe = "https://old.tyuiu.ru/shedule_new/bin/groups.py?act=show&print=&sgroup="  + group
    return render_template("schedule.html", iframe=iframe)

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
