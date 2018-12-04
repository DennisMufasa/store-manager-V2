"""flask app factory to be called to create an object of the app"""
# system import
import os
# third-party imports
from flask import Flask
# local import
from ...instance.config import configure

def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configure[config])
    app.secret_key = os.urandom(24)
    # register version blueprint onto app
    from .v2 import v2_blueprint

    app.register_blueprint(v2_blueprint)
    return app
