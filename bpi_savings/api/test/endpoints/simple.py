import logging

from flask import request
from flask_restplus import Resource
from bpi_savings.api.restplus import api

ns = api.namespace('api/test/simple', description='Test the API Framework')


@ns.route('/')
class Simple(Resource):
    def get(self):
        return 'Test Successful'
