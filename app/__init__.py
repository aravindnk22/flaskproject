from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app.catalog import catalog
from app.auth import auth
import app.config as conf
import configparser,os
from ast import literal_eval as leval

db = SQLAlchemy()

def createapp(config_type):

    app = Flask(__name__)
    configs = configparser.ConfigParser()
    configs.read('app/config/config.ini')
    config_dict = dict(configs.items(section=config_type))

    app.config['DEBUG'] = leval(config_dict['debug'])
    app.config['SECRET_KEY'] = config_dict['secret_key']
    app.config['SQLALCHEMY_DATABASE_URI'] = config_dict['sqlalchemy_database_uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = leval(config_dict['sqlalchemy_track_modifications'])
    app.config['SQLALCHEMY_ECHO'] = leval(config_dict['sqlalchemy_echo'])
    app.config['SQLALCHEMY_PRE_PING'] = leval(config_dict['sqlalchemy_pre_ping'])

    app.register_blueprint(catalog)
    app.register_blueprint(auth)

    db.init_app(app)

    return app


print("Initialization completed")
