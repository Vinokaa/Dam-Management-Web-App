# sensor.py
from flask import Blueprint, request, render_template
from flask_login import current_user, login_required
from models.iot.sensor import Sensor
from models.iot.actuator import Actuator
from models.iot.kit import Kit

devices_bp = Blueprint("sensor", __name__, template_folder="templates")

@devices_bp.route('/register_sensor')
@login_required
def register_sensor():
    return render_template("register_sensor.html", session=current_user.role)

@devices_bp.route('/add_sensor', methods=['POST'])
@login_required
def add_sensor():
    if request.method == 'POST':
        sensor = request.form['sensor']
        topic = request.form['topic']
        measure_unit = request.form["measure_unit"]
        Sensor.create_sensor(sensor, topic, measure_unit, None)

    return devices()

@devices_bp.route('/del_sensor', methods=['GET', 'POST'])
@login_required
def del_sensor():
    if request.method == 'POST':
        id = request.form['id']
    else:
        id = request.args.get('id', None)

    Sensor.delete_sensor(id)

    return devices()

@devices_bp.route('/register_actuator')
@login_required
def register_actuator():
    return render_template("register_actuator.html", session=current_user.role)

@devices_bp.route('/add_actuator', methods=['POST'])
@login_required
def add_actuator():
    if request.method == 'POST':
        actuator = request.form['actuator']
        topic = request.form['topic']
        measure_unit = request.form["measure_unit"]
        Actuator.create_actuator(actuator, topic, measure_unit, None)

    return devices()

@devices_bp.route('/del_actuator', methods=['GET', 'POST'])
@login_required
def del_actuator():
    if request.method == 'POST':
        id = request.form['id']
    else:
        id = request.args.get('id', None)

    Actuator.delete_actuator(id)

    return devices()

@devices_bp.route('/devices')
@login_required
def devices():
    sensors = Sensor.get_sensors()
    actuators = Actuator.get_actuators()

    if current_user.role == "admin":
        return render_template("devicesAdmin.html", sensores=sensors, atuadores=actuators, session=current_user.role)
    else:
        return render_template("devices.html", sensores=sensors, atuadores=actuators, session=current_user.role)
