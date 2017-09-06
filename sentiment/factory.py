from flask import Flask
# from flask_restful import Api


def create_app(config=None):
    app = Flask('sentiment')

    app.config.from_object('sentiment.config')

    app.config.update(config or {})

    register_db(app)
    register_cli(app)
    register_api(app)

    return app


def register_db(app):
    from .model import db
    db.init_app(app)


def register_cli(app):
    from .model import db

    @app.cli.command("initdb")
    def init_db():
        import sentiment.model.all  # make sure all models are imported
        db.create_all()


def register_api(app):
    pass
