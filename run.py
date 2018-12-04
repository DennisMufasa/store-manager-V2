"""Running an instance of the application"""
# system import 
import os
# local import
from .app.api import create_app

config_name = os.getenv('APP_SETTINGS')     # exported APP_SETTINGS='development'
app = create_app(config_name)


if __name__ == "__main__":
    app.run()