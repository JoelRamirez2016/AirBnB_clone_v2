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
    """display HBNB in route '/hbnb'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display “C” followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return "C " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run()
