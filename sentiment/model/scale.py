from . import db


class Scale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    lower_limit = db.Column(db.Integer)
    upper_limit = db.Column(db.Integer)
    hidden = db.Column(db.Boolean, default=False)

    measurements = db.relationship('Measurement', back_populates='scale')

    def __contains__(self, item):
        """check wether a value is in the range of the scale"""
        if self.lower_limit is not None and self.upper_limit is not None:
            return self.lower_limit <= item <= self.upper_limit
        elif self.lower_limit is not None:
            return item >= self.lower_limit
        elif self.upper_limit is not None:
            return item <= self.upper_limit
        else:
            return True
