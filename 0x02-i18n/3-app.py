#!/usr/bin/env python3
"""
using babel and a function get_locale
"""
from flask_babel import Babel
from flask import Flask, g, request, render_template


class Config():
    """configuration for a flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get the users locale configurations"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """return the index page"""
    return render_template("3-index.html")
