#!/usr/bin/env python3
"""This module defines a basic babel setup app"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_locale() -> str:
    """Get locale from a request"""
    return request.accept_languages.best_match(Config.LANGUAGES)


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>)"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
