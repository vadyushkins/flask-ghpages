import flask

__all__ = ["create_app"]


def create_app():
    app = flask.Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route("/")
    def index():
        return "hello world"

    return app
