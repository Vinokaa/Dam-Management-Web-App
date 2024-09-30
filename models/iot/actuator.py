from models.db import db
from models.iot.device import Device
from models.iot.kit import Kit

class Actuator(db.Model):
    __tablename__ = "actuator"
    device_id = db.Column(db.Integer, db.ForeignKey(Device.id), primary_key=True, nullable=False)

    def create_actuator(name, topic, measure_unit, kit_id):
        device = Device(name=name, topic=topic, measure_unit=measure_unit, kit_id=kit_id)
        db.session.add(device)
        db.session.commit()

        actuator = Actuator(device_id=device.id)
        db.session.add(actuator)
        db.session.commit()
        
    def delete_actuator(id):
        actuator = Actuator.query.filter(Actuator.device_id == id).first()
        device = Device.query.filter(Device.id == id).first()

        if device is not None:
            db.session.delete(actuator)
            db.session.commit()
            db.session.delete(device)
            db.session.commit()

    def get_actuators():
        actuators = Actuator.query.join(Device, Device.id == Actuator.device_id).add_columns(Device.id, Device.name, Device.value, Device.topic, Device.measure_unit, Device.kit_id).all()

        return actuators

    def get_actuator_id(id):
        return Actuator.query.filter(Actuator.id == id).first()
    
    def get_actuator_value(name):
        device = Device.query.filter(Device.name == name).first()
        return device.value

    def update_actuator(name, value):
        device = Device.query.filter(Device.name == name).first()
        device.value = value

        db.session.commit()