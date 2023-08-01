#!/usr/bin/env python3
"""
using babel and a function get_locale
"""
from flask_babel import Babel
from flask import Flask, request, render_template, g
from datetime import datetime
from pytz import timezone
import pytz.exceptions
import locale

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """configuration for a flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    user_id = request.args.get('login_as')
    if user_id:
        try:
            user = users.get(int(user_id))
        except ValueError:
            user = None
        return user
    else:
        return None


@app.before_request
def before_request():
    """get user before request"""
    user = get_user()
    g.user = user

    time_now = pytz.utc.localize(datetime.utcnow())
    time = time_now.astimezone(timezone(get_timezone()))  # type: ignore
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    time_format = "%b %d, %Y %I:%M:%S %p"
    g.time = time.strftime(time_format)


@babel.localeselector
def get_locale():
    """get the users locale configurations"""
    locale = request.args.get("locale")
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    locale = request.headers.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """find the timezone of the user"""
    time = request.args.get("timezone")
    if time:
        try:
            return timezone(time).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        time = g.user.get('timezone')
        try:
            return timezone(time).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_TIMEZONE']


@app.route("/")
def index():
    """return the index page"""
    return render_template("index.html", time=g.time)
