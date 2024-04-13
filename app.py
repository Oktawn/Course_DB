from flask import Flask, render_template, request, redirect, url_for, session
from config import app, db
from User import User


@app.route("/home", methods=["GET", "POST"])
def home(user):
    return render_template("home.html", user=user)


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    user = User
    if request.method == "POST":
        login = request.form("login")
        pswd = request.form("pswd")
        check = user.query.filter_by(username=login).first()
        if "butSign" in request.form:
            if not check:
                user.Authoriz(login, pswd)
                try:
                    db.session.add(user)
                    db.session.commit()
                    redirect("/home", user)
                except:
                    return render_template("login.html")
            else:
                render_template(
                    "login.html", error="данный пользователь уже существует"
                )

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    return login()


if __name__ == "__main__":
    app.run(debug=True)
