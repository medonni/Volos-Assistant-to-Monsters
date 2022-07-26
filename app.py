from flask import Flask
from main import main_bp
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.secret_key = 'TheSuperSecretKeyThatNooneKnows'
app.debug = True
app.register_blueprint(main_bp)
toolbar = DebugToolbarExtension(app)


if __name__ == '__main__':
    app.run()