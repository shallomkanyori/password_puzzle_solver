"""Main Flask app for Password Puzzle Solver."""
from flask import Flask, render_template, request, abort, url_for
from flask_cors import CORS
from models import storage
import utils
import json


app = Flask(__name__)
app.logger.setLevel('INFO')
app.url_map.strict_slashes = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


# @app.teardown_appcontext
# def close_db(error):
#     """Close database session."""
#     storage.close()


@app.route("/", methods=['GET', 'POST'])
def start():
    """Serves the game or the start page depending on the method."""

    if request.method == 'POST':
        difficulty = int(request.form["difficulty"])
        word = utils.get_random_word(difficulty)
        if word:
            return render_template("game.html", word=word)
        else:
            abort(500)

    return render_template("start.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
