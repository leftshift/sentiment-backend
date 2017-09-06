from . import db


class Tagset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    hidden = db.Column(db.Boolean, default=False)

    tags = db.relationship('Tag', back_populates='tagset')
