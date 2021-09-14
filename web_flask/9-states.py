#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def states(state_id=""):
    """display a HTML page with a list of states"""

    states = storage.all(State)

    if state_id:
        for state in states.values():
            if state.id == state_id:
                return render_template("9-states.html", state=state)
        return render_template("9-states.html")
    return render_template("9-states.html", states=states)


@app.teardown_appcontext
def teardown(e):
    """close the current session."""
    storage.close()

if __name__ == "__main__":
    app.run()
