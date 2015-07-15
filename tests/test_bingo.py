"""Unit tests for cat2cohort."""

import unittest
from bingo import bingo


class TestBingoGenerator(unittest.TestCase):

    """Test methods from bingo."""

    def test_bingo_generator_has_default_size(self):
        bingo_generator = bingo.BingoGenerator()
        expected = pow(bingo.DEFAULT_SIZE, 2)
        self.assertEquals(bingo_generator.size, expected)

    def test_bingo_generator_has_given_size(self):
        bingo_generator = bingo.BingoGenerator(4)
        self.assertEquals(bingo_generator.size, 16)

    def test_select_words_should_have_the_right_size(self):
        test_size = 2
        bingo_generator = bingo.BingoGenerator(size=test_size)
        seed_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        bingo_generator.words = seed_list
        selection = bingo_generator.select_words()
        self.assertEquals(len(selection), pow(test_size, 2))

    def test_select_words_should_return_words_from_the_seed_list(self):
        test_size = 2
        bingo_generator = bingo.BingoGenerator(size=test_size)
        seed_list = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
        bingo_generator.words = seed_list
        selection = set(bingo_generator.select_words())
        self.assertTrue(seed_list.difference(selection))
