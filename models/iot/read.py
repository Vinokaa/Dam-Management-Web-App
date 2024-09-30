from models.db import db
from models.iot.sensor import Sensor
from models.iot.device import Device
from datetime import datetime
from sqlalchemy import desc

class Read(db.Model):
    __tablename__ = "read"
    datetime = db.Column(db.DateTime(), primary_key=True, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey(Sensor.device_id), nullable=False)

    def save_read(sensor_id, read):
        db.session.add(Read(datetime=datetime.now(), value=read, sensor_id=sensor_id))
        db.session.commit()

    def get_read(start, stop):
        return Read.query.filter(Read.datetime >= start, Read.datetime <= stop).all()
    
    def get_last_dist():
        return Read.query.join(Device, Device.id == Read.sensor_id).filter(Device.name == "HC-SR04").order_by(Read.datetime.desc()).first()
