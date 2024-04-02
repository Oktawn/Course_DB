from flask import Flask, render_template, request, url_for, session,redirect

app = Flask(__name__)

@app.route("/")
def home():
    #our code will co here
    return render_template("home.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    #our code will co here
    return render_template("login.html")

@app.route("/logout")
def logout():
    #our code will co here
    return redirect(url_for("login.html"))


if __name__ == '__main__':
    app.run(debug=True)