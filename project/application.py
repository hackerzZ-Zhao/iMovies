from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
import os

app = Flask(__name__)
manager = Manager(app)

app.config.from_pyfile('config/base_setting.py')
if 'ops_config' in os.environ:
    app.config.from_pyfile('config/{}_setting.py'.format(os.environ['ops_config']))

db = SQLAlchemy(app)

