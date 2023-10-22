
Here are two versions of the script with different appearances:

Script 1: Version 1

python
Copy code
#!/usr/bin/python3
"""
Starts a Flask web application with various routes.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """
    Returns the message "Hello HBNB!"
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
Script 2: Version 2

python
Copy code
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
