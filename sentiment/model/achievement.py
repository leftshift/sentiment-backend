from . import db


class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    checks = db.relationship('Check', back_populates='achievement')
