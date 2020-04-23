from flask import Blueprint
from web_root import settings
from web_root.api.restplus import api
from web_root.api.test.endpoints.simple import ns as simple_ns
from web_root.api.test.endpoints.categories import ns as blog_categories_ns
from web_root.api.test.endpoints.posts import ns as blog_posts_ns
from web_root.database import db


api_bp = Blueprint('api', __name__, url_prefix='/api')

api.init_app(api_bp)
api.add_namespace(simple_ns)
api.add_namespace(blog_posts_ns)
api.add_namespace(blog_categories_ns)



