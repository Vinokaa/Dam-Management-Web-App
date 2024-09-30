from flask import Flask, render_template, request, redirect, url_for, jsonify, Blueprint
from flask_login import current_user, login_required

comandos_bp = Blueprint("comandos", __name__, template_folder="templates")

@comandos_bp.route("/comandos")
@login_required
def comandos():
    return render_template("comandos.html", session=current_user.role)