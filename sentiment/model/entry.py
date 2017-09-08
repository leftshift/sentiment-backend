from . import db


class Entry(db.Model):
    """A single diary entry"""
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates="entries")

    measurements = db.relationship('Measurement', back_populates='entry')
    checks = db.relationship('Check', back_populates='entry')
    tags = db.relationship(
        'Tag',
        secondary='entry_tag',
        back_populates='entries'
    )
