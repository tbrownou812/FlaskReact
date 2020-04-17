from flask import Flask
from web.app import blueprint

app = Flask(__name__)


def main():
    app.register_blueprint(blueprint)
    app.run(debug=True)


if __name__ == "__main__":
    main()
