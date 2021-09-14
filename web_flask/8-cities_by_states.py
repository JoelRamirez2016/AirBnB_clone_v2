#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """display a HTML page with a list of cities"""
    return render_template("8-cities_by_states.html", states=storage.all(State))


@app.teardown_appcontext
def teardown(e):
    """close the current session."""
    storage.close()

if __name__ == "__main__":
    app.run()
