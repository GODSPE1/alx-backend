#!/usr/bin/env python3
"""This module defines a basic flask app"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>"""
    return render_template('0-index.html', title='Welcome to Holberton')


if __name__ == '__main__':
    app.run(debug=True)
