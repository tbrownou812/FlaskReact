# Flask Settings
SERVER_NAME = 'localhost:8888'
FLASK_DEBUG = True

# Flask-RestPlus Settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy Settings
# SQLALCHEMY_DATABASE_URI = 'sqlite:///database/db.sqlite'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:P%40ssw0rd%21@localhost:5432/test'
SQLALCHEMY_TRACK_MODIFICATIONS = False
