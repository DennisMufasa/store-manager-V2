"""create version 2 blueprint"""
# third-party import
from flask import Blueprint
# blueprint for version 2
v2_blueprint = Blueprint('v2', __name__, url_prefix='/api/v2')
# import views
from . import views