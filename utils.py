"""Helper functions."""


def get_word(difficulty):
    """Returns a random word of the given difficulty.

    Args:
        difficulty(int): The difficulty of the random word to get.
    """
    if difficulty not in range(1, 4):
        return None

    word = storage.get_random_word(difficulty)

    if not word:
        return None

    word['word'] = word['word'].upper()

    return word
