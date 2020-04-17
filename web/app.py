from flask import Blueprint

blueprint = Blueprint('web', __name__, template_folder='templates', static_folder='static', url_prefix='/web')


@blueprint.route('/')
def hello_world():
    return 'Hello World!'

