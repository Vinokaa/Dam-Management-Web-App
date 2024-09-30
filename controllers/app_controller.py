from flask import Flask, render_template, request, jsonify, url_for
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from threading import Lock
from flask_login import LoginManager, current_user, login_required
import json

from controllers.login_controller import login
from controllers.devices_controller import devices_bp
from controllers.temporeal_controller import tempoReal
from controllers.comandos_controller import comandos_bp
from controllers.kits_controller import kits_bp
from controllers.reads_controller import read_bp
from models.db import db, instance

from models.iot.write import Write
from models.iot.sensor import Sensor
from models.iot.actuator import Actuator
from models.iot.read import Read
from models.user.user import User

def distToCircle(dist):
        return int((400 - dist) * 0.5825)

dists = [0, 0]
att = False

thread = None
thread_lock = Lock()

def create_app():
    app = Flask(__name__, template_folder="./views", static_folder="./static", root_path="./")

    app.register_blueprint(login, url_prefix='/')
    app.register_blueprint(tempoReal, url_prefix='/')
    app.register_blueprint(devices_bp, url_prefix='/')
    app.register_blueprint(comandos_bp, url_prefix='/')
    app.register_blueprint(kits_bp, url_prefix='/')
    app.register_blueprint(read_bp, url_prefix='/')

    app.config["TESTING"] = False
    app.config["SECRET_KEY"] = "generated-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "/"
    login_manager.init_app(app)

    app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''
    app.config['MQTT_PASSWORD'] = ''
    app.config['MQTT_KEEPALIVE'] = 5000
    app.config['MQTT_TLS_ENABLED'] = False

    mqtt_client = Mqtt()
    mqtt_client.init_app(app)

    socketio = SocketIO(app)

    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Conectado ao broker')
            mqtt_client.subscribe("barragem-13-sensors")
        else:
            print('Bad connection. Code:', rc)

    @mqtt_client.on_disconnect()
    def handle_disconnect(client, userdata, rc):
        print("Disconnected from broker")

    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        global dists, att, dht22, led, servo
        js = json.loads(message.payload.decode())

        if js["type"] == "update":
            dists[0] = dists[1]
            dists[1] = js["dist"]

            with app.app_context():
                Sensor.update_sensor("HC-SR04", dists[1])
                Sensor.update_sensor("DHT22", js["hum"])
                Actuator.update_actuator("LED", js["led"])
                Actuator.update_actuator("Servo", js["srv"])

            dht22 = js["hum"]

            if js["led"]:
                led = "LIGADO"
            else:
                led = "DESLIGADO"
            
            if js["srv"]:
                servo = 0
            else:
                servo = 180
            
            att = True
        else:
            socketio.emit("listCall", {"ativar-led": js["ativar-led"], "ativar-servo": js["ativar-servo"], "ativar-led-chuva": js["ativar-led-chuva"], "ativar-servo-chuva": js["ativar-servo-chuva"]})
        

    @app.route("/executarComando", methods=["GET", "POST"])
    def executarComando():
        request_data = request.get_json()

        if(request_data["comando"] == ""):
            return jsonify("error")
        
        if request_data["comando"] == "list" or request_data["comando"].split()[0] == "chg":
            Write.save_datetime(request_data["comando"], current_user.id)
            publish_result = mqtt_client.publish("barragem-13-actuators", request_data["comando"])
            return jsonify(publish_result)


    @socketio.on('connect')
    def connect():
        global thread
        print('Client connected')

        with thread_lock:
            if thread is None:
                thread = socketio.start_background_task(background_thread)

    @socketio.on('disconnect')
    def disconnect():
        print('Client disconnected',  request.sid)

    def background_thread():
        global dists, att, dht22, led, servo
        print("Thread enviando")
        while True:
            if att:
                socketio.emit('updateSensorData', {'last_dist': distToCircle(dists[0]), "new_dist": distToCircle(dists[1]), "value": dists[1], "dht22": dht22, "led": led, "servo": servo})
                att = False
                with app.app_context():
                    Read.save_read(Sensor.get_sensor_name("HC-SR04").id, dists[0])
                socketio.sleep(1)
                with app.app_context():
                    Read.save_read(Sensor.get_sensor_name("DHT22").id, dht22)
                socketio.sleep(3)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    def index():
        return render_template("login.html")

    @app.route('/home')
    @login_required
    def homeAdmin():
        return render_template("home.html", session=current_user.role)

    @app.route('/credenInvalida')
    def credenInvalida():
        return render_template("credenInvalida.html")

    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    return app
