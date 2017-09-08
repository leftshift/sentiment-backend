from . import db


class Check(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Boolean, default=False, nullable=False)

    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'), nullable=False)
    entry = db.relationship('Entry', back_populates='checks')

    achievement_id = db.Column(db.Integer, db.ForeignKey('achievement.id'), nullable=False)
    achievement = db.relationship('Achievement', back_populates='checks')
