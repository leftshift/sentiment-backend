from sqlalchemy.ext.hybrid import hybrid_property

from . import db


entry_tag = db.Table(
    'entry_tag',
    db.Column('entry_id', db.Integer, db.ForeignKey('entry.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(50), nullable=False)
    hidden = db.Column(db.Boolean, default=False)

    tagset_id = db.Column(db.Integer, db.ForeignKey('tagset.id'), nullable=False)
    tagset = db.relationship('Tagset', back_populates='tags')

    entries = db.relationship(
        'Entry',
        secondary='entry_tag',
        back_populates='tags'
    )

    def __init__(self, *args, **kwargs):
        if 'tagset' in kwargs:
            # Make sure tagset is set first
            self.tagset = kwargs.pop('tagset')

        super().__init__(*args, **kwargs)

    @hybrid_property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        assert self.tagset is not None, "name can't be set before tagset"
        tag_with_same_name = Tag.query.filter(
            Tag.tagset_id == self.tagset_id,
            Tag.name == name
        ).first()
        assert not tag_with_same_name or self is tag_with_same_name,\
            "tag with this name already exists in tagset"
        self._name = name
