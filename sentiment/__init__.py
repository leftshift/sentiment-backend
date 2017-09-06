from flask import Flask
from flask_restful import Api

from .model import db
import sentiment.model.all

# from .api import Entry


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db.init_app(app)

# api.add_resource(Entry, '/entry', '<int:id>')


@app.route("/")
def test():
    return str(User.query.all())


@app.cli.command("initdb")
def init_db():
    db.create_all()
