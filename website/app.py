import flask

__all__ = ["app"]

app = flask.Flask(__name__)
app.config.from_pyfile('settings.py')

@app.route("/")
def index():
    return flask.render_template('base.html', title='Hello World!')
