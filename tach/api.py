from safrs import SAFRSAPI

from .flask import app
from . import models

api = SAFRSAPI(app, prefix='/api')
with app.app_context():
    api.expose_object(models.Circular)
