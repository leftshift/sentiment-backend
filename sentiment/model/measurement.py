from sqlalchemy.ext.hybrid import hybrid_property

from . import db


class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _value = db.Column(db.Integer, nullable=False)

    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'), nullable=False)
    entry = db.relationship('Entry', back_populates='measurements')

    scale_id = db.Column(db.Integer, db.ForeignKey('scale.id'), nullable=False)
    scale = db.relationship('Scale', back_populates='measurements')

    def __init__(self, *args, **kwargs):
        if 'scale' in kwargs:
            # Make sure scale is set first
            self.scale = kwargs.pop('scale')

        super().__init__(*args, **kwargs)

    @hybrid_property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self.scale is not None:
            # This can only be checked if a scale is already set.
            assert value in self.scale
            self._value = value
        else:
            raise ValueError("value cannot be set before scale")
