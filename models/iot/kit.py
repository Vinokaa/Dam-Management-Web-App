from models.db import db

class Kit(db.Model):
    __tablename__ = "kit"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    def create_kit(name):
        db.session.add(Kit(name=name))
        db.session.commit()
    
    def get_kits():
        return Kit.query.filter(Kit.is_active == True).all()

    def remove_kit(id):
        kit = Kit.query.filter(Kit.id == id).first()
        kit.is_active = False

        db.session.commit()

    def get_id_by_name(name):
        return Kit.query.filter(Kit.name == name).first().id
    
    def get_kit_by_id(id):
        return Kit.query.filter(Kit.id == id).first()
    
    def change_kit(id, name):
        kit = Kit.query.filter(Kit.id == id).first()
        kit.name = name

        db.session.commit()