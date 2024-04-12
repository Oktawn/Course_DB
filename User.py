from config import db

class User():
    login = db.Column(db.String, primary_key=True)
    pswd = db.Column(db.String, nullable=False)
    fname = db.Column(db.String, default="")
    lname = db.Column(db.String, default="")
    group = db.Column(db.INTEGER)
    email = db.Column(db.String, nullable=False)
    policy = db.Column(db.INTEGER, default=0)

    def SignUp(login, pswd, email):
        User.login = login
        User.pswd = pswd
        User.email = email

    def SignIn(email,pswd):
        User.email=email
        User.pswd=pswd

    def __repr__(self):
        return "<User %r>" % self.login
