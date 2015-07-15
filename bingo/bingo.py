import random

DEFAULT_SIZE = 5


class BingoGenerator(object):

    """Generating bingo grid."""

    def __init__(self, size=DEFAULT_SIZE):
        self.words = None
        self.size = pow(size, 2)

    def select_words(self):
        return random.sample(self.words, self.size)
