# -*- coding: utf-8 -*-

import os
from string import Template, ascii_uppercase
import itertools


class CardMaker(object):

    def __init__(self, size):
        self.size = size
        self.elements = []

    def make_card(self):
        raise NotImplemented()


class MarkdownCardMaker(CardMaker):

    def make_card(self):
        res = []
        for row_index in range(self.size):
            row_items = self.elements[row_index:row_index + self.size]
            res.append(self.make_row(row_items))
        return '\n'.join(res)

    def make_row(self, elements):
        return "|".join(elements)


class LaTeXCardMaker(CardMaker):

    def read_template(self):
        path = os.path.dirname(os.path.realpath(__file__))
        template_file = os.path.join(path, 'tex', 'template.tex')
        return open(template_file, 'r').read()

    def make_card(self):
        contents = self.make_card_contents()
        return contents

    def make_card_contents(self):
        template = Template(self.read_template())
        node_definitions = self.make_node_definitions()
        values = {
            'title': "Wikimania 2015 bingo",
            'size': self.size,
            'sequence': '1/A, 2/B, 3/C, 4/D, 5/E',
            'node_definitions': "\n".join(node_definitions)
        }
        return template.safe_substitute(values)

    def get_node_list(self):
        alphabet = ascii_uppercase
        letters = alphabet[0:self.size]
        cartesian_product = itertools.product(letters, letters)
        node_list = ['%s%s' % (x, y) for (x, y) in cartesian_product]
        node_list.remove('CC')
        return node_list

    def make_node_definitions(self):
        nodes = self.get_node_list()
        return [self.make_element(x, y) for (x, y) in zip(nodes, self.elements)]

    def make_element(self, index, contents):
        element = r"\newcommand{\Node%s}{%s}" % (index, contents)
        return element
