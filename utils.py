"""Helper functions."""
from models import storage
from random import choice


def get_random_word(difficulty):
    """Returns a random word of the given difficulty.

    Args:
        difficulty(int): The difficulty of the random word to get.
    """
    if difficulty not in range(1, 4):
        return None

    words = storage.find('words', {'difficulty': difficulty})
    if not words:
        return None

    words = list(words)
    if len(words) == 0:
        return None

    word = choice(words)
    if not word:
        return None

    del word['_id']
    word['word'] = word['word'].upper()

    return word
