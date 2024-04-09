from flask import Flask, render_template, request, url_for, session, redirect

app = Flask(__name__)
app.config.from_object("config.py")
from app import views


@app.route("/")
def home():
    user = {"nickname": "Oktawn", "policy": "student"}
    return render_template("home.html", user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    # our code will co here
    return render_template("login.html")


@app.route("/logout")
def logout():
    # our code will co here
    return redirect(url_for("login.html"))


if __name__ == "__main__":
    app.run(debug=True)
