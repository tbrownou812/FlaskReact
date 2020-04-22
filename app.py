import os
import logging.config

from flask import Flask
from web.views import web_bp


app = Flask(__name__, root_path='web/')
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), './logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure(flask_app):
    flask_app.config['SERVER_NAME'] = 'localhost:8888'

    flask_app.register_blueprint(web_bp)


def run_server():
    configure(app)

    log.info('>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=True)


if __name__ == "__main__":
    run_server()
else:
    configure()
