#!/usr/bin/python3
"""Starts a Flask web_application.

The application listens on 0.0.0.0; port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DatabaseStorage.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """It displays an HTML page with a list of all State objects in Database Storage.

    States are sorted according to name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Delete the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
