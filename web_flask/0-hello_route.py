#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

# create a Flask application instance
app = Flask(__name__)


# define a route for the root URL
@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return "Hello HBNB!"


# entry point of the application to be ran on a specific port
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=None)
