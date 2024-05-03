from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from check_db import create_user, check_user, get_data_user, change_transcript,create_table
from werkzeug.security import generate_password_hash

class RestrForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField()

class TranscriptForm(FlaskForm):
    transcript = IntegerField("Integer number")
    submit = SubmitField()

app = Flask(__name__)
app.config["SECRET_KEY"] = "the random string"

# Главная страница ученика
@app.route("/home/<username>", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home(username):
    student = get_data_user(username)
    group_id = student[-1]
    transcript = student[-3]
    name_error = 'нету номера зачетки'
    print(transcript)
    print(student)
    return render_template("new_home.html", user=username, group = group_id, transcript = transcript, name_error = name_error)

# Оценки 
@app.route('/transcript')
def transcript():
    return render_template("evalution.html")

# Расписание
@app.route('/schedule/<group>', methods=["GET", "POST"])
def schedule(group):
    iframe = "https://old.tyuiu.ru/shedule_new/bin/groups.py?act=show&print=&sgroup="  + group
    return render_template("schedule.html", iframe=iframe)

# Внести номер зачетки
@app.route('/evaluations_input/<username>', methods=["GET", "POST"])
def evaluations_input(username):
    form_transcript = TranscriptForm()
    if form_transcript.validate_on_submit():
        transcript_num = form_transcript.transcript.data 
        change_transcript(username, transcript_num)
    return render_template('evaluations_input.html', form = form_transcript, user = username)


# Ошибка
@app.route("/error", methods=["GET", "POST"])
@app.route("/error/<name_error>", methods=["GET", "POST"])
def error(name_error):
    return render_template("error.html", name_error = name_error)

# Основная страница
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    create_table()
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
