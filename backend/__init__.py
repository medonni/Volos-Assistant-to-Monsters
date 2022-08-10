from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


toolbar = DebugToolbarExtension()

def create_app():
    app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
    app.secret_key = 'TheSuperSecretKeyThatNooneKnows'
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
    toolbar.init_app(app)

    register_blueprints(app)

    return app


def register_blueprints(app):
    from backend.main import main_bp
    app.register_blueprint(main_bp)