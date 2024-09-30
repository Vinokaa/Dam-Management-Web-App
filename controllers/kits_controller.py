from flask import Blueprint, request, render_template, redirect
from models.iot.kit import Kit
from models.iot.sensor import Sensor
from models.iot.actuator import Actuator
from models.iot.device import Device
from models.logs.admin_modifies_kit import Admin_modifies_kit

from flask_login import current_user, login_required

kits_bp = Blueprint("kit", __name__, template_folder="templates")

@kits_bp.route("/kits")
@login_required
def kits():
    if current_user.role == "admin":
        kits = Kit.get_kits()
        return render_template("listar_kits.html", kits=kits)
    else:
        return redirect("/home")

@kits_bp.route('/del_kit', methods=['GET', 'POST'])
@login_required
def del_kit():
    if current_user.role == "admin":
        if request.method == 'POST':
            id = request.form['id']
        else:
            id = request.args.get('id', None)

        Kit.remove_kit(id)

        return kits()
    else:
        return redirect("/home")

@kits_bp.route("/register_kit")
@login_required
def register_kit():
    if current_user.role == "admin":
        devices = Device.get_unchecked()
        return render_template("register_kit.html", devices=devices)
    else:
        return redirect("/home")

@kits_bp.route("/add_kit", methods=["GET", "POST"])
@login_required
def add_kit():
    if current_user.role == "admin":
        name = request.form["name"]
        devices = request.form.getlist("checkbox")
        Kit.create_kit(name)

        kit_id = Kit.get_id_by_name(name)
        if devices is not None:
            for i in devices:
                Device.set_kit(i, kit_id)

        return kits()
    else:
        return redirect("/home")
    
@kits_bp.route("/edit_kit")
@login_required
def edit_kit():
    id = request.args.get("id", None)
    requested_kit = Kit.get_kit_by_id(id)

    devices_checked = Device.get_checked(id)
    devices_unchecked = Device.get_unchecked()
    return render_template("editar_kit.html", kit=requested_kit, session=current_user.role, checked=devices_checked, unchecked=devices_unchecked)

@kits_bp.route("/change_kit", methods=['GET', 'POST'])
@login_required
def change_kit():
    if request.method == 'POST':
        id = request.form["id"]
        name = request.form["name"]
        devices = request.form.getlist("checkbox")
        linked_devices = Device.get_checked(id)

        if linked_devices is not None:
            for i in linked_devices:
                Device.unlink_kit(i.id)

        Kit.change_kit(id, name)

        if devices is not None:
            for i in devices:
                Device.set_kit(i, id)

        Admin_modifies_kit.save_datetime(current_user.id, id)

    return kits()