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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    The default value of text is “is cool”"""
    return "Python " + text.replace("_", " ")

if __name__ == "__main__":
    app.run()
