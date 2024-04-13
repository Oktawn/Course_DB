from config import db

class User(db):
    login = db.Column(db.String, primary_key=True)
    pswd = db.Column(db.String, nullable=False)
    policy = db.Column(db.INTEGER, default=0)

    def Authoriz(login, pswd):
        User.login = login
        User.pswd = pswd



    def Logout():
        User.login=None
        User.pswd=None


    def __repr__(self):
        return "<User %r>" % self.login
    
