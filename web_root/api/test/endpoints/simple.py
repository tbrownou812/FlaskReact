from flask_restplus import Resource
from web_root.api import api

ns = api.namespace('api/simple', description='Test the API Framework')


@ns.route('/')
class Simple(Resource):
    def get(self):
        return 'Test Successful'
