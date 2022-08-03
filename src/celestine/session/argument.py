"""Parse arguments."""
import argparse

from celestine import module

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import CELESTINE
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import TASK
from celestine.keyword.main import application
from celestine.keyword.main import language


class Argument():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog=CELESTINE
        )

        self.parser.add_argument(
            APPLICATION,
            choices=application,
            help="Select which application to run.",
        )

        self.parser.add_argument(
            "-l, --language",
            choices=language,
            help="Choose a language.",
            dest=LANGUAGE,
        )

        self.subparser = self.parser.add_subparsers(
            dest=TASK,
            required=True,
        )
