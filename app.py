from flask import Flask, render_template, request, redirect, url_for, session
from config import Config
from flask_bcrypt import Bcrypt
from db import (
    init_db,
    check_student,
    show_grade,
    show_group,
    update_student,
    show_schedule,
    show_assignment,
)

app = Flask(__name__)

app.config.from_object(Config)
bcrypt = Bcrypt(app)


init_db()


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["email"]
        password = request.form["password"]
        user = check_student(username, password, bcrypt)
        if user:
            session["email"] = user
            print(session["email"])
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("email", None)
    return redirect(url_for("login"))


@app.route("/main")
def index():
    cur = "Главная"
    return render_template("index.html", page=cur)


@app.route("/main/my", methods=["GET", "POST"])
def profile():
    if "email" not in session:
        return redirect(url_for("login"))
    user = session["email"]
    cur = "Личные данные"
    group = show_group(user["group_id"])
    if request.method == "POST":
        user["first_name"] = request.form["first_name"]
        user["last_name"] = request.form["last_name"]
        update_student(user["first_name"], user["last_name"], user["email"])
        return redirect(url_for("profile"))
    return render_template("profile.html", user=user, group=group, page=cur)


@app.route("/main/grades", methods=["GET", "POST"])
def grades():
    if "email" not in session:
        return redirect(url_for("login"))
    cur = "Оценки"
    grades = show_grade(session["email"]["id"])
    return render_template("grades.html", grades=grades, page=cur)


@app.route("/main/schedule", methods=["GET", "POST"])
def schedule():
    if "email" not in session:
        return redirect(url_for("login"))
    cur = "Расписание"
    content = show_schedule(session["email"]["group_id"])
    return render_template("schedule.html", html_content=content, page=cur)


@app.route("/main/assignment", methods=["GET", "POST"])
def assignment():
    if "email" not in session:
        return redirect(url_for("login"))
    cur = "Задания"
    content = show_assignment(session["email"]["id"])
    return render_template("assignment.html", page=cur, grades=content)


if __name__ == "__main__":
    app.run(debug=True)
