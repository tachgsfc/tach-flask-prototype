from flask_sqlalchemy import SQLAlchemy
from safrs import SAFRSBase
import sqlalchemy as sa
import sqlalchemy_utils as su

from .core.xml_alchemy import XMLType
from .flask import app

db = SQLAlchemy(app)


class Circular(SAFRSBase, db.Model):
    number = sa.Column(sa.Integer, primary_key=True)
    sender = sa.Column(su.EmailType, nullable=False)
    received = sa.Column(sa.DateTime, nullable=False)
    subject = sa.Column(sa.UnicodeText, nullable=False)
    body = sa.Column(sa.UnicodeText, nullable=False)


class Voevent(SAFRSBase, db.Model):
    content = sa.Column(XMLType, nullable=False)
    ivorn = sa.Column(su.URLType,
                      sa.Computed(sa.func.xpath('/*/@ivorn', content)),
                      primary_key=True)
