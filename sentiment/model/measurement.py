from sqlalchemy.ext.hybrid import hybrid_property

from . import db


class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _value = db.Column(db.Integer, nullable=False)

    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'), nullable=False)
    entry = db.relationship('Entry', back_populates='measurements')

    scale_id = db.Column(db.Integer, db.ForeignKey('scale.id'), nullable=False)
    scale = db.relationship('Scale', back_populates='measurements')

    @hybrid_property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        assert value in self.scale
        self._value = value
