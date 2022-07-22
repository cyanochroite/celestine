"""Parse arguments."""
import argparse

from celestine.keyword.main import CELESTINE

from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import language

from celestine.keyword.main import PACKAGE
from celestine.keyword.main import package

from celestine.keyword.main import PYTHON
from celestine.keyword.main import python


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
    "-p, --package",
    choices=package,
    help="Choose a mode to opperate in.",
    dest=PACKAGE,
)

parser.add_argument(
    "-v, --version",
    choices=python,
    help="Tell me which python version you are using.",
    dest=PYTHON,
)


subparser = parser.add_subparsers(
    title="configuration",
    description="Generate configuration files.",
    prog="celestine_configuration",
    dest="configuration",
    required=False,
    help="Enter the data for the configuration file.",
)


parser_preferences = subparser.add_parser(
    "preferences",
    help="Try: english tkinter python_3_10",
)

parser_preferences.add_argument(
    "language",
    choices=language,
    help="The natural language to display the application in.",
)

parser_preferences.add_argument(
    "package",
    choices=package,
    help="Which subpackage to run as the primary application.",
)

parser_preferences.add_argument(
    "python",
    choices=python,
    help="Which version of python to run as.",
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


argument = parser.parse_args()
