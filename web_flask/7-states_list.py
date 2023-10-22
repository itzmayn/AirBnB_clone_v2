#!/usr/bin/python3
"""
Flask web app for displaying a sorted list of states.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states-list', strict_slashes=False)
def list_states():
    """
    This function generates an HTML page listing states in a well-structured manner.
    It retrieves state records from the storage, performs sorting, and provides them to the '7-states_list.html' template.
    """
    states = sorted(list(storage.all("State").values(), key=lambda x: x.name))
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close_storage_on_teardown(exception):
    """
    This function ensures that the storage connection is appropriately closed when the Flask app context is dismantled.
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
