from flask import Blueprint
from bpi_savings import settings
from bpi_savings.api.restplus import api
from bpi_savings.api.test.endpoints.simple import ns as test_namespace


blueprint = Blueprint(settings.BP_NAME, __name__, template_folder='templates', static_folder='static',
                      url_prefix=settings.URL_PREFIX)

api.init_app(blueprint)
api.add_namespace(test_namespace)