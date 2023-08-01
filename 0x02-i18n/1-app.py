#!/usr/bin/env python3
"""
simple flask app that utilises config
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """configuration for a flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index():
    """return the index page"""
    return render_template("1-index.html")

if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
