"""Unit tests for cat2cohort."""

import unittest
from bingo import bingo


class TestBingoGenerator(unittest.TestCase):

    """Test methods from bingo."""

    def test_bingo_generator_has_default_size(self):
        bingo_generator = bingo.BingoGenerator()
        self.assertEquals(bingo_generator.size, 20)

    def test_bingo_generator_has_given_size(self):
        bingo_generator = bingo.BingoGenerator(5)
        self.assertEquals(bingo_generator.size, 5)
