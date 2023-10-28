from flask import Flask
from store.config import configurations
from store.extensions import db

def create_app(environment_name='dev'):
    app = Flask(__name__)
    app.config.from_object(configurations[environment_name])
    db.init_app(app)
    return app


