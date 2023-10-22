#!/usr/bin/python3
"""
This script starts a Flask web application for displaying states and cities.
"""

# Import necessary modules and classes
from models import storage

from flask import Flask, render_template
from models import *

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for '/cities_by_states'
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    This function displays a list of states and their associated cities in alphabetical order.
    It retrieves states from the storage and passes them to the '8-cities_by_states.html' template.
    """
    # Retrieve states from the storage
    states = storage.all("State").values()
    
    # Render the '8-cities_by_states.html' template and pass states to it
    return render_template('8-cities_by_states.html', states=states)

# Define a teardown function for the Flask app context
@app.teardown_appcontext
def teardown_db(exception):
    """
    This function ensures the storage is closed when the Flask app context is torn down.
    """
    storage.close()

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
