from flask import Blueprint

web_bp = Blueprint('web', __name__, template_folder='templates', static_folder='static', url_prefix='/web')


@web_bp.route('/')
def hello_world():
    return 'Hello World!'

