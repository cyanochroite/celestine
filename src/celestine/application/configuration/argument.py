"""Generate configuration files for all packages."""
import argparse

from celestine.keyword.main import CELESTINE

from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import language

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import application

from celestine.keyword.main import PYTHON
from celestine.keyword.main import python


parser = argparse.ArgumentParser()


parser.add_argument(
    "_",
    choices="configuration",
    help="Eat the first argument.",
)

subparser = parser.add_subparsers(
    title="configuration",
    description="Generate configuration files.",
    prog="celestine_configuration",
    dest="configuration",
    required=True,
    help="Enter the data for the configuration file.",
)

parser_celestine = subparser.add_parser(
    CELESTINE,
    help="Try: english tkinter python_3_10",
)

parser_celestine.add_argument(
    APPLICATION,
    choices=application,
    help="Which subpackage to run as the primary application.",
)

parser_celestine.add_argument(
    LANGUAGE,
    choices=language,
    help="The natural language to display the application in.",
)

parser_celestine.add_argument(
    PYTHON,
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
