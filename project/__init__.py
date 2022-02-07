from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_mqtt import Mqtt
from dotenv import dotenv_values


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
socketio = SocketIO()
mqtt = Mqtt()
setup = dotenv_values('.env_local')
app = Flask(__name__)

def create_app(debug=False):

    app.debug = debug
    
    app.config['SECRET_KEY'] = setup['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = setup['SQLALCHEMY_DATABASE_URI']
    app.config['TEMPLATES_AUTO_RELOAD']=(setup['TEMPLATES_AUTO_RELOAD']=="True")
    app.config['MQTT_BROKER_URL']=setup['MQTT_BROKER_URL']
    app.config['MQTT_BROKER_PORT']=int(setup['MQTT_BROKER_PORT'])
    app.config['MQTT_USERNAME']=setup['MQTT_USERNAME']
    app.config['MQTT_PASSWORD']=setup['MQTT_PASSWORD']
    app.config['MQTT_KEEPALIVE']=int(setup['MQTT_KEEPALIVE'])
    app.config['MQTT_TLS_ENABLED']=(setup['MQTT_TLS_ENABLED']=="True")

    app.app_context().push()
    db.init_app(app)
    


    from .main.models import User
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))


    # blueprint for auth routes in our app
    from .main.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    mqtt.init_app(app)
    socketio.init_app(app)

    return app

