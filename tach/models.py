from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
import sqlalchemy_utils as su

from .flask import app

db = SQLAlchemy(app)


class Circular(db.Model):
    number = sa.Column(sa.Integer, primary_key=True)
    sender = sa.Column(su.EmailType, nullable=False)
    received = sa.Column(sa.DateTime, nullable=False)
    subject = sa.Column(sa.UnicodeText, nullable=False)
    body = sa.Column(sa.UnicodeText, nullable=False)
