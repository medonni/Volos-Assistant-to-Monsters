from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

toolbar = DebugToolbarExtension()
db = SQLAlchemy()


def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
    app.secret_key = 'TheSuperSecretKeyThatNooneKnows'
    app.debug = True

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'backend/data/cards.data')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    register_blueprints(app)

    toolbar.init_app(app)

    db.init_app(app)
    Migrate(app, db)

    return app


def register_blueprints(app):
    from backend.main_bp import main_bp
    app.register_blueprint(main_bp)