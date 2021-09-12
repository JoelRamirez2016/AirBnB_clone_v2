#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """display Hello HBNB! in route '/'"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display HBNB! in route '/hbnb'"""
    return "HBNB!"

if __name__ == "__main__":
    app.run()
