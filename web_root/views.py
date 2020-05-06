from flask import Blueprint
from datetime import datetime
from flask import render_template
# from web_root import web_bp


web_bp = Blueprint('web', __name__, template_folder='templates', static_folder='static')

# @web_bp.route('/')
# def hello_world():
#     return 'Hello World!'


@web_bp.route('/')
@web_bp.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year
    )


@web_bp.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@web_bp.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


