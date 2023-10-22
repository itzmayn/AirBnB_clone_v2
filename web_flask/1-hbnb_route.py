#!/usr/bin/python3
"""
This script initializes a Flask web application with various routes.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """
    This route returns the message "Hello HBNB!"
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This route returns the message "HBNB"
    """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
