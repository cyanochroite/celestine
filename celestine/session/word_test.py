""""""

import unittest

from celestine.session.word import parser_formatter


class word_test(unittest.TestCase):
    """"""

    def test_parser_error(self):
        """"""
        first = "usage: "
        second = parser_formatter("usage")
        self.assertEqual(first, second)

