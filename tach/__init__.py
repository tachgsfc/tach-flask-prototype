from flask.cli import FlaskGroup

from .flask import app
from . import models
from . import api


main = FlaskGroup(create_app=lambda: app).main
