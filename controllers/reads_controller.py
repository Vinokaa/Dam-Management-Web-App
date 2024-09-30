#reads_controller.py
from flask import Blueprint, render_template, request
from models.iot.read import Read
from models.iot.sensor import Sensor
from models.iot.device import Device
from flask_login import current_user, login_required
from models.logs.login import Login
from models.logs.admin_modifies_user import Admin_modifies_user
from models.logs.admin_modifies_kit import Admin_modifies_kit
from models.iot.read import Read
from models.iot.write import Write
from models.user.user import User
from models.iot.kit import Kit

read_bp = Blueprint("read", __name__, template_folder="views")

@read_bp.route("/history")
@login_required
def history_read():
    sensors = Sensor.get_sensors()
    read = {}
    return render_template("history.html", session=current_user.role)

@read_bp.route("/search", methods=['POST'])
@login_required
def search():
    if request.method == 'POST':
        option = request.form['option']
        start = request.form['start']
        stop = request.form['stop']
        logs = {}
        
        if option == "login":
            logins = Login.get_logins(start, stop)
            if logins is not None:
                for i in logins:
                    logs[i.login] = str(i.name) + " logou"
                    if i.logout is not None:
                        logs[i.logout] = str(i.name) + " deslogou"
        elif option == "modUser":
            mods = Admin_modifies_user.get_datetime(start, stop)
            if mods is not None:
                for i in mods:
                    user = User.search_user_id(i.user_id).name
                    admin = User.search_user_id(i.admin_user_id).name
                    logs[i.datetime] = admin + " modificou " + user
        elif option == "modKit":
            mods = Admin_modifies_kit.get_datetime(start, stop)
            if mods is not None:
                for i in mods:
                    kit = Kit.get_kit_by_id(i.kit_id).name
                    admin = User.search_user_id(i.admin_user_id).name
                    logs[i.datetime] = admin + " modificou " + kit
        elif option == "read":
            reads = Read.get_read(start, stop)
            if reads is not None:
                for i in reads:
                    valor = i.value
                    sensor = Device.get_name_by_id(i.sensor_id)
                    logs[i.datetime] = str(sensor) + " leu " + str(valor)
        elif option == "write":
            writes = Write.get_write(start, stop)
            if writes is not None:
                for i in writes:
                    comando = i.value
                    operator = User.search_user_id(i.operator_id).name
                    logs[i.datetime] = str(operator) + " executou " + str(comando)

        return render_template("history.html", session=current_user.role ,logs=logs)