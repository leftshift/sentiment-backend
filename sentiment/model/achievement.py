from . import db


class Achivement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Boolean, default=False)

    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'), nullable=False)
    entry = db.relationship('Entry', back_populates='achivements')
