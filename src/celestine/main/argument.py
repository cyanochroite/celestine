"""Parse arguments."""
import argparse

from celestine.main.keyword import CELESTINE

from celestine.main.keyword import LANGUAGE
from celestine.main.keyword import language

from celestine.main.keyword import PACKAGE
from celestine.main.keyword import package

from celestine.main.keyword import PYTHON
from celestine.main.keyword import python


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
