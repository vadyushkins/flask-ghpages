import flask_frozen

import website

if __name__ == "__main__":
    freezer = flask_frozen.Freezer(website.app)

    freezer.freeze()
