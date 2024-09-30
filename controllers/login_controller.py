from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import current_user, logout_user
from models.user.user import User
from models.logs.login import Login
from models.logs.admin_modifies_user import Admin_modifies_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required

login = Blueprint("login", __name__, template_folder="templates")

@login.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']

        user_search = User.search_user_name(user)
        
        if user_search is not None and user_search.is_active and check_password_hash(user_search.password, password):
            login_user(user_search, remember=True)
            Login.save_login(user_search.id)

            return render_template("home.html", session=current_user.role)
        else:
            return render_template("credenInvalida.html")
    else:
        return render_template('login.html')
    
@login.route("/logout", methods=["POST", "GET"])
@login_required
def logout():
    Login.save_logout(current_user.id)
    logout_user()
    return redirect("/")
    
@login.route('/users')
@login_required
def listar_user():
    if current_user.role == "admin":
        users = User.get_users()
        return render_template("listar_user.html", users=users, session=current_user.role)
    else:
        return redirect("/home")

@login.route('/register_user')
@login_required
def register_user():
    return render_template("register_user.html", session=current_user.role)

@login.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        role = request.form["role"]
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
        role = request.args.get('role', None)

    if User.get_user_by_name(user):
        return redirect("/")

    User.create_user(user, generate_password_hash(password, method="pbkdf2:sha256"), role)
    
    
    return listar_user()

@login.route("/edit_user")
@login_required
def edit_user():
    id = request.args.get("id", None)
    requested_user = User.search_user_id(id)
    return render_template("editar_user.html", user=requested_user, session=current_user.role)

@login.route("/change_user", methods=['GET', 'POST'])
@login_required
def change_user():
    if request.method == 'POST':
        id = request.form["id"]
        user = request.form['user']
        password = request.form['password']
        role = request.form["role"]
    else:
        id = request.args.get("id", None)
        user = request.args.get('user', None)
        password = request.args.get('password', None)
        role = request.args.get('role', None)
    
    User.modify_user(id, user, generate_password_hash(password, method="pbkdf2:sha256"), role)
    Admin_modifies_user.save_datetime(current_user.id, id)

    return listar_user()

@login.route('/del_user', methods=['GET', 'POST'])
@login_required
def del_user():
    if request.method == 'POST':
        id = request.form["id"]
    else:
        id = request.args.get("id", None)
    
    User.remove_user(id)

    return listar_user()