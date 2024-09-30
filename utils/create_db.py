from flask import Flask
from models import *
from werkzeug.security import generate_password_hash

def create_db(app:Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()
        User.create_user("admin", generate_password_hash("admin", method='pbkdf2:sha256'), "admin")
        Kit.create_kit("Padrão")
        Sensor.create_sensor("HC-SR04", "barragem-13-send", "cm", 1)
        Sensor.create_sensor("DHT22", "barragem-13-send", "º", 1)
        Actuator.create_actuator("LED", "barragem-13-receive", "", 1)
        Actuator.create_actuator("Servo", "barragem-13-receive", "º", 1)