"""Main Flask app for Password Puzzle Solver."""
from flask import Flask, render_template, request, abort
from models import storage

import json
import requests


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(error):
    """Close database session."""
    storage.close()


@app.route("/", methods=['GET', 'POST'])
def start():
    """Serves the game or the start page depending on the method."""

    if request.method == 'POST':
        difficulty = int(request.form["difficulty"])
        url = "http://localhost:5001/api/v1/word/{}".format(difficulty)

        res = requests.get(url)

        if res.status_code == 200:
            word = res.json()
            return render_template("game.html", word=word)
        else:
            abort(500)

    return render_template("start.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
