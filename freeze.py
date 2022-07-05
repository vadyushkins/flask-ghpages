import flask_frozen

from website import create_app

if __name__ == '__main__':
    app = create_app()
    freezer = flask_frozen.Freezer(app)

    freezer.freeze()