"""Parse arguments."""
import argparse

from celestine.keyword.main import CELESTINE


from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import language

from celestine.keyword.main import PYTHON
from celestine.keyword.main import python

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import application

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import application

from celestine.keyword.main import TASK

parser = argparse.ArgumentParser(prog=CELESTINE)

parser.add_argument(
    APPLICATION,
    choices=application,
    help="Tell me which python version you are using.",
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

subparser = parser.add_subparsers(dest=TASK, required=True)
