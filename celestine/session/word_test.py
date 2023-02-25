""""""

import unittest

from celestine.session.word import (
    parser_error,
    parser_formatter,
    parser_parser_error,
    parser_value,
)


class Word(unittest.TestCase):
    """"""

    def test_parser_error(self):
        """"""
        argument = "argument"
        name = "name"
        message = "message"

        first = parser_error(argument, name, message)
        second = "argument name: message"
        self.assertEqual(first, second)

    def test_parser_error_none(self):
        """"""
        argument = "argument"
        name = None
        message = "message"

        first = parser_error(argument, name, message)
        second = "message"
        self.assertEqual(first, second)

    def test_parser_formatter(self):
        """"""
        usage = "usage"

        first = parser_formatter(usage)
        second = "usage: "
        self.assertEqual(first, second)

    def test_parser_parser_error(self):
        """"""
        program = "program"
        error = "error"
        message = "message"

        first = parser_parser_error(program, error, message)
        second = "program: error: message\n"
        self.assertEqual(first, second)

    def test_parser_value(self):
        """"""
        choice = "choice"
        value = "value"
        choose = "choose"
        choices = ["one", "two"]

        first = parser_value(choice, value, choose, choices)
        second = "choice: 'value' (choose 'one', 'two')"
        self.assertEqual(first, second)
