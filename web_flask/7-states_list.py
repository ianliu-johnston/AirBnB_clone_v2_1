#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage
"""
Very Simple Flask hello world
"""


app = Flask(__name__)


@app.route('/states_list')
def hello_HBNB():

    """
    :wq
    """
    return (render_template('7-states_list.html', states=storage.all("State").values()))

@app.teardown_appcontext
def teardown(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
