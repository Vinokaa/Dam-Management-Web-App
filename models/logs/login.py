from models.db import db
from models.user.user import User
from datetime import datetime

class Login(db.Model):
    __tablename__ = "login"
    login = db.Column(db.DateTime(), primary_key=True, nullable=False)
    logout = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def save_login(user_id):
        user = User.query.filter(User.id == user_id).first()

        login = Login(login=datetime.now(), user_id=user.id)

        db.session.add(login)
        db.session.commit()

    def save_logout(user_id):
        user = User.query.filter(User.id == user_id).first()

        login = Login.query.filter(Login.user_id == User.id, Login.logout == None).first()

        login.logout = datetime.now()

        db.session.commit()
    
    def get_logins(start, stop):
        return Login.query.filter(Login.login >= start, Login.login <= stop).join(User, User.id == Login.user_id).add_columns(Login.login, Login.logout, User.name).all()