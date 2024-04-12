from flask import Flask, render_template, request, redirect, url_for, session
from config import app, db
from User import User

user = User


@app.route("/home", methods=["GET", "POST"])
def home():
    user = {"nickname": user.login, "policy": user.policy}
    return render_template("home.html", user=user)


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form("login")
        pswd = request.form("pswd")
        email = request.form("email")

        user.SignUp(login, pswd, email)
        try:
            db.session.add(user)
            db.session.commit()
            redirect("/home")
        except:
            request.form("login").args.get()

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    # our code will co here
    return login()


if __name__ == "__main__":
    app.run(debug=True)
