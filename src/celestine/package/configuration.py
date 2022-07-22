"""Generate configuration files for all packages."""
import os.path
import sys

directory = os.path.dirname(sys.path[0])
sys.path.append(directory)

import argparse
import configparser

from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_save
from celestine.main.configuration import configuration_celestine
from celestine.main.configuration import configuration_translator

from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CONFIGURATION_CELESTINE
from celestine.keyword.main import CONFIGURATION_TRANSLATOR


from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import language

from celestine.keyword.main import PACKAGE
from celestine.keyword.main import package

from celestine.keyword.main import PYTHON
from celestine.keyword.main import python

from celestine.keyword.translator import FILE


from celestine.keyword.main import language


parser = argparse.ArgumentParser(
    prog="celestine_configuration"
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
    "celestine",
    help="Try: english tkinter python_3_10",
)

parser_celestine.add_argument(
    "language",
    choices=language,
    help="The natural language to display the application in.",
)

parser_celestine.add_argument(
    "package",
    choices=package,
    help="Which subpackage to run as the primary application.",
)

parser_celestine.add_argument(
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


parse = parser.parse_args()
configuration = parse.configuration

if configuration == "celestine":
    configuration_save(
        configuration_celestine(
            parse.language,
            parse.package,
            parse.python,
        ),
        directory,
        CELESTINE,
        CONFIGURATION_CELESTINE,
    )

if configuration == "translator":
    configuration_save(
        configuration_translator(
            parse.key,
            parse.region,
            parse.url,
        ),
        directory,
        CELESTINE,
        CONFIGURATION_TRANSLATOR,
    )
