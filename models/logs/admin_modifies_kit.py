from models.db import db
from models.user.user import User
from models.iot.kit import Kit
from datetime import datetime

class Admin_modifies_kit(db.Model):
    __tablename__ = "admin_modifies_kit"
    datetime = db.Column(db.DateTime(), primary_key=True, nullable=False)
    admin_user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    kit_id = db.Column(db.Integer, db.ForeignKey(Kit.id), nullable=False)

    def save_datetime(admin_id, kit_id):
        admin_modifies_kit = Admin_modifies_kit(datetime=datetime.now())
        admin = User.query.filter(User.id == admin_id).first()
        kit = Kit.query.filter(Kit.id == kit_id).first()

        admin_modifies_kit.admin_user_id = admin.id
        admin_modifies_kit.kit_id = kit.id

        db.session.add(admin_modifies_kit)
        db.session.commit()

    def get_datetime(start, stop):
        return Admin_modifies_kit.query.filter(Admin_modifies_kit.datetime >= start, Admin_modifies_kit.datetime <= stop).all()