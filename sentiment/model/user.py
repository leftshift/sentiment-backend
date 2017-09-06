from sqlalchemy.ext.hybrid import hybrid_property

from ..security import pwd_context
from . import db


class User(db.Model):
    """A User"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    _password_hash = db.Column(db.String(120), nullable=False)

    entries = db.relationship('Entry', back_populates='user')

    @hybrid_property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, value):
        self._password_hash = pwd_context.hash(value)

    def check_password(self, password):
        return pwd_context.verify(password, self._password_hash)
