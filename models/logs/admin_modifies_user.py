from models.db import db
from models.user.user import User
from datetime import datetime

class Admin_modifies_user(db.Model):
    __tablename__ = "admin_modifies_user"
    datetime = db.Column(db.DateTime(), nullable=False, primary_key=True)
    admin_user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def save_datetime(admin_id, user_id):
        admin_modifies_user = Admin_modifies_user(datetime=datetime.now())
        admin = User.query.filter(User.id == admin_id).first()
        user = User.query.filter(User.id == user_id).first()

        admin_modifies_user.admin_user_id = admin.id
        admin_modifies_user.user_id = user.id

        db.session.add(admin_modifies_user)
        db.session.commit()

    def get_datetime(start, stop):
        return Admin_modifies_user.query.filter(Admin_modifies_user.datetime >= start, Admin_modifies_user.datetime <= stop).all()