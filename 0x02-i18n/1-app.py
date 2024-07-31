#!/usr/bin/env python3
"""This module defines a basic babel setup app"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>)"""
    return render_template('0-index.html', title='Welcome to Holberton')


if __name__ == '__main__':
    app.run(debug=True)
