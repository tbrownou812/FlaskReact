from flask import Blueprint
from web_root import settings
from web_root.api.restplus import api
from web_root.api.test.endpoints.simple import ns as test_namespace


blueprint = Blueprint('web', __name__, template_folder='templates', static_folder='static')

api.init_app(blueprint)
api.add_namespace(test_namespace)

