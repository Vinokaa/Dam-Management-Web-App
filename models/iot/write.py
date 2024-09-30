from models.db import db
from models.iot.actuator import Actuator
from models.user.user import User
from datetime import datetime

class Write(db.Model):
    __tablename__ = "write"
    datetime = db.Column(db.DateTime(), primary_key=True, nullable=False)
    value = db.Column(db.String(50), nullable=False)
    operator_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def save_datetime(comando, operator_id):
        db.session.add(Write(datetime=datetime.now(), value=comando, operator_id=operator_id))
        db.session.commit()

    def get_write(start, stop):
        return Write.query.filter(Write.datetime >= start, Write.datetime <= stop).all()