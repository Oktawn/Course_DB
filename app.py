from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///DataBase.db"
db = SQLAlchemy(app)


class UserDB(db.Model):
    login = db.Column(db.String, primary_key=True)
    pswd = db.Column(db.String, nullable=False)
    policy = db.Column(db.INTEGER, default=0)

    def Authoriz(login, pswd):
        login = login
        pswd = pswd

    def Logout():
        login = None
        pswd = None

    def __repr__(self):
        return "<User %r>" % self.login


@app.route("/home", methods=["GET", "POST"])
def home(user):
    return render_template("home.html", user)


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form["login"]
        pswd = request.form["pswd"]

        user = UserDB(login=login, pswd=pswd, policy=0)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect("/home", user)
        except:
            render_template("login.html")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    return login()


if __name__ == "__main__":
    app.run(debug=True)
