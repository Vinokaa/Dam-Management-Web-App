from models.db import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(102), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    def create_user(name, password, role):
        user = User(name=name, password=password, role=role)
        db.session.add(user)

        db.session.commit()

    def modify_user(user_id, name, password, role):
        user = User.query.filter(User.id == user_id).first()
        user.name = name
        user.password = password
        user.role = role
        db.session.commit()
    
    def remove_user(user_id):
        user = User.query.filter(User.id == user_id).first()

        user.is_active = False

        db.session.commit()

    def get_users():
        users = User.query.filter(User.is_active == True).all()

        return users
    
    def search_user_name(name):
        user = User.query.filter(User.name == name).first()

        return user
    
    def search_user_id(id):
        user = User.query.filter(User.id == id).first()

        return user
    
    def get_user_by_name(name):
        return User.query.filter(User.name == name).first()