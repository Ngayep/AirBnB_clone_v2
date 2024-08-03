#!/usr/bin/python3
""" a script that starts a Flask web application
with 3 routes
"""


from flask import Flask
app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return a certain string"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """return "C" with some value"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
