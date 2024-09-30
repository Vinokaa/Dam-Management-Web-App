from models.db import db
from models.iot.kit import Kit

class Device(db.Model):
    __tablename__ = "device"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Integer, nullable=False, default=0)
    topic = db.Column(db.String(60), nullable=False)
    measure_unit = db.Column(db.String(3), nullable=False)
    kit_id = db.Column(db.Integer, db.ForeignKey(Kit.id))

    def set_kit(name, kit_id):
        device = Device.query.filter(Device.name == name).first()
        device.kit_id = kit_id

        db.session.commit()

    def get_checked(kit_id):
        return Device.query.filter(Device.kit_id == kit_id).all()
    
    def get_unchecked():
        return Device.query.filter(Device.kit_id == None).all()
    
    def unlink_kit(id):
        device = Device.query.filter(Device.id == id).first()
        device.kit_id = None

        db.session.commit()

    def get_name_by_id(id):
        return Device.query.filter(Device.id == id).first().name