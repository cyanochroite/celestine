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

argument = parser.parse_args()
