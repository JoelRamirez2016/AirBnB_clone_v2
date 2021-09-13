#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display a HTML page with a list of states"""
    return render_template("7-states_list.html", states=storage.all(State))

@app.teardown_appcontext
def teardown(e):
    """close the current session."""
    storage.close()

if __name__ == "__main__":
    app.run()
