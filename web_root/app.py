import os
import logging.config

from flask import Flask, Blueprint
from web_root import settings
from web_root.views import web_bp as web_bp
from web_root import api_bp as api_bp

from web_root.database import db

from web_root.api.restplus import api


app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), './logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure(flask_app):
    flask_app.config['SERVER_NAME'] = settings.SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

    flask_app.register_blueprint(web_bp)
    flask_app.register_blueprint(api_bp)

    db.init_app(flask_app)


def run_server():
    configure(app)

    log.info('>>>>> Starting development server at http://{}/ <<<<<'.format(settings.SERVER_NAME))
    app.run(debug=True)


if __name__ == "__main__":
    run_server()
else:
    configure()
