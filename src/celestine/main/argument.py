"""Parse arguments."""
import argparse

from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CURSES
from celestine.keyword.main import DEARPYGUI
from celestine.keyword.main import TKINTER
from celestine.keyword.main import UNITTEST

from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import language

from celestine.keyword.main import PACKAGE
from celestine.keyword.main import package

from celestine.keyword.main import PYTHON
from celestine.keyword.main import python

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import application


parser = argparse.ArgumentParser(
    prog=CELESTINE
)


parser.add_argument(
    "-l, --language",
    choices=language,
    help="Choose a language.",
    dest=LANGUAGE,
)


parser.add_argument(
    "-v, --version",
    choices=python,
    help="Tell me which python version you are using.",
    dest=PYTHON,
)



subparser = parser.add_subparsers(
    title="application",
    description="Generate configuration files.",
    prog="celestine_configuration",
    dest=APPLICATION,
    required=False,
    help="Enter the data for the configuration file.",
)


parser_configuration = subparser.add_parser(
    "configuration",
    help="Try: english tkinter python_3_10",
)

parser_configuration.add_argument(
    "language",
    choices=language,
    help="The natural language to display the application in.",
)

parser_configuration.add_argument(
    "package",
    choices=package,
    help="Which subpackage to run as the primary application.",
)

parser_configuration.add_argument(
    "python",
    choices=python,
    help="Which version of python to run as.",
)





parser_celestine = subparser.add_parser(
    CELESTINE,
    help="Help text.",
)



parser_curses = subparser.add_parser(
    CURSES,
    help="Help text.",
)




parser_dearpygui = subparser.add_parser(
    DEARPYGUI,
    help="Help text.",
)




parser_tkinter = subparser.add_parser(
    TKINTER,
    help="Help text.",
)




parser_translator = subparser.add_parser(
    "translator",
    help="Try: english tkinter python_3_10",
)

parser_translator.add_argument(
    "key",
    help="The natural language to display the application in.",
)

parser_translator.add_argument(
    "region",
    help="Which subpackage to run as the primary application.",
)

parser_translator.add_argument(
    "url",
    help="Which version of python to run as.",
)





parser_unittest = subparser.add_parser(
    UNITTEST,
    help="Help text.",
)



argument = parser.parse_args()
