import os
import logging.config

from flask import Flask
from web.views import web_bp


app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), './logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure():
    app.config['SERVER_NAME'] = 'localhost:8888'
    app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    app.config['ERROR_404_HELP'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_BINDS'] = {
        'rest_api_demo': 'sqlite:///db.sqlite'
    }

    app.register_blueprint(web_bp)


def run_server():
    configure()

    log.info('>>>>> Starting development server at http://{}/web/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=True)


if __name__ == "__main__":
    run_server()
else:
    configure()
