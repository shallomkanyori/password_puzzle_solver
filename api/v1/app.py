#!/usr/bin/python3
"""Flask application for the Password Puzzle Solver API."""
from flask import Flask, abort, jsonify
from models import storage
from os import environ

app = Flask(__name__)
app.config['JSONFIY_PRETTYPRINT_REGULAR'] = True


@app.teardown_appcontext
def close_db(error):
    """Close database session."""
    storage.close()


@app.route('/api/v1/word/<int:difficulty>')
def get_word(difficulty):
    """Returns a random word of the given difficulty.

    Args:
        difficulty(int): The difficulty of the random word to get.
    """
    if difficulty not in range(1, 4):
        abort(404)

    word = storage.get_random_word(difficulty)

    if not word:
        abort(404)

    return jsonify(word)


if __name__ == "__main__":
    host = environ.get('PWD_SOLVER_API_HOST', '0.0.0.0')
    port = environ.get('PWD_SOLVER_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
