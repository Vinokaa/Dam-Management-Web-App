from models.db import db
from models.iot.device import Device
from models.iot.kit import Kit

class Sensor(db.Model):
    __tablename__ = "sensor"
    device_id = db.Column(db.Integer, db.ForeignKey(Device.id), primary_key=True, nullable=False)

    def create_sensor(name, topic, measure_unit, kit_id):
        device = Device(name=name, topic=topic, measure_unit=measure_unit, kit_id=kit_id)
        db.session.add(device)
        db.session.commit()

        sensor = Sensor(device_id=device.id)
        db.session.add(sensor)
        db.session.commit()
            
    def delete_sensor(id):
        sensor = Sensor.query.filter(Sensor.device_id == id).first()
        device = Device.query.filter(Device.id == id).first()

        if device is not None:
            db.session.delete(sensor)
            db.session.commit()
            db.session.delete(device)
            db.session.commit()

    def get_sensors():
        sensors = Sensor.query.join(Device, Device.id == Sensor.device_id).add_columns(Device.id, Device.name, Device.value, Device.topic, Device.measure_unit, Device.kit_id).all()

        return sensors
    
    def get_sensor_name(name):
        device = Device.query.filter(Device.name == name).first()

        return device

    def get_sensor_value(name):
        device = Device.query.filter(Device.name == name).first()
        return device.value

    def update_sensor(name, value):
        device = Device.query.filter(Device.name == name).first()
        device.value = value

        db.session.commit()