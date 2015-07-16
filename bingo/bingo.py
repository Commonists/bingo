import random

DEFAULT_SIZE = 5


class BingoGenerator(object):

    """Generating bingo grid."""

    def __init__(self, size=DEFAULT_SIZE):
        self.words = None
        self.size = pow(size, 2)
        self.maker = None

    def select_words(self):
        res = random.sample(self.words, self.size)
        return res

    def create_lots_of_selection(self, number):
        selection = []
        while len(selection) <= number:
            sample = random.sample(self.words, self.size)
            if sample not in selection:
                selection.append(sample)
            else:
                print "Duplicate"
        return selection

    def make_lots_of_cards(self, number):
        selection = self.create_lots_of_selection(number)
        for item in selection:
            self.maker.elements = item
            yield self.maker.make_card()

    def make_card(self):
        self.maker.elements = self.select_words()
        return self.maker.make_card()
