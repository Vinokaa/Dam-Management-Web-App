from flask import Flask, render_template, request, redirect, url_for, jsonify, Blueprint
from flask_login import current_user, login_required
from models.iot.sensor import Sensor
from models.iot.actuator import Actuator
from models.iot.read import Read

tempoReal = Blueprint("tempoReal", __name__, template_folder="templates")

def distToCircle(dist):
    return int((400 - dist) * 0.5825)

#dists = [0, 150]
att = False

@tempoReal.route("/temporeal")
@login_required
def temporeal():
    sensors = Sensor.get_sensors()
    actuators = Actuator.get_actuators()
    last_dist = Read.get_last_dist()
    if last_dist is not None:
        return render_template("tempo-real.html", last_fill=distToCircle(sensors[0].value), new_fill=distToCircle(sensors[0].value), dist=sensors[0].value, actuators=actuators, sensors=sensors, session=current_user.role)
    else:
        return render_template("tempo-real.html", last_fill=distToCircle(0), new_fill=distToCircle(0), dist=0, actuators=actuators, sensors=sensors, session=current_user.role)