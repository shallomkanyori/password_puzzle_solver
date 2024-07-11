"""Routes for word CRUD operations."""
from app import app
from flask import abort, jsonify
from models import storage
import utils


@app.route('/api/v1/word/<int:difficulty>')
def get_word(difficulty):
    """Returns a random word of the given difficulty.

    Args:
        difficulty(int): The difficulty of the random word to get.
    """
    word = utils.get_word(difficulty)

    if not word:
        abort(404)

    return jsonify(word)
