from time import timezone
from flask import Flask
from backend.data.generate_data import daily_data_download
import os
from flask_apscheduler import APScheduler

scheduler = APScheduler()


def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
    app.secret_key = 'TheSuperSecretKeyThatNooneKnows'
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False

    scheduler.init_app(app)
    scheduler.start()

    @scheduler.task('cron', id='daily_data_download_task', hour='9')
    def cronjob():
        daily_data_download()


    register_blueprints(app)


    return app


def register_blueprints(app):
    from backend.main_bp import main_bp
    app.register_blueprint(main_bp)