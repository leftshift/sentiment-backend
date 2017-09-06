import os
import tempfile
import pytest
from datetime import datetime

from sentiment.factory import create_app


@pytest.fixture
def app(request):
    _, temp_db_location = tempfile.mkstemp()
    config = {
        'SQLALCHEMY_DATABASE_URI': "sqlite:///" + temp_db_location,
        'TESTING': True,
    }

    app = create_app(config=config)

    with app.app_context():
        import sentiment.model.all
        from sentiment.model import db
        db.create_all()

        yield app


@pytest.fixture
def db(app):
    from sentiment.model import db
    yield db


@pytest.fixture
def user(models):
    yield models.User(username="test", password="test")


@pytest.fixture
def entry(models, user):
    yield models.Entry(time=datetime.now(), text="blah", user=user)


@pytest.fixture
def models():
    import sentiment.model.all
    yield sentiment.model.all


def test_user(db, models):
    u = models.User(username="test", password="test")
    assert u.check_password("test") is True
    assert u.check_password("uaaf") is False
    db.session.add(u)
    db.session.commit()


def test_entry(db, models, user):
    e = models.Entry(time=datetime.now(), text="blah")
    user.entries.append(e)
    assert e in user.entries
    assert user is e.user

    s = models.Scale(name="scale")
    m = models.Measurement(scale=s)
    m.value = 3

    e.measurements.append(m)
    assert m in e.measurements
    assert e is m.entry


def test_measurement(db, models, entry):
    s = models.Scale(name="scale")
    with pytest.raises(ValueError):
        m = models.Measurement(value=5)
    m = models.Measurement(scale=s, value=5)
    m.entry = entry

    db.session.add(m)
    db.session.commit()

    assert s is models.Scale.query.first()
    assert m in s.measurements
    assert s is m.scale
    assert m.value is 5


def test_scale_limits(db, models):
    pass
    s = models.Scale(name="scale", upper_limit=10)
    m = models.Measurement(scale=s, value=0)
    with pytest.raises(AssertionError):
        m.value = 20
    m.value = -3

    s = models.Scale(name="scale", lower_limit=-5)
    m = models.Measurement(scale=s, value=0)
    with pytest.raises(AssertionError):
        m.value = -10
    m.value = -5

    s = models.Scale(name="scale", lower_limit=-5, upper_limit=5)
    m = models.Measurement(scale=s, value=0)
    with pytest.raises(AssertionError):
        m.value = -6
    with pytest.raises(AssertionError):
        m.value = 10
    m.value = -5
    m.value = 5
