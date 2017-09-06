from . import db


entry_tag = db.Table(
    'entry_tag',
    db.Column('entry_id', db.Integer, db.ForeignKey('entry.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    hidden = db.Column(db.Boolean, default=False)

    tagset_id = db.Column(db.Integer, db.ForeignKey('tagset.id'), nullable=False)
    tagset = db.relationship('Tagset', back_populates='tags')

    entries = db.relationship(
        'Entry',
        secondary='entry_tag',
        back_populates='tags'
    )
