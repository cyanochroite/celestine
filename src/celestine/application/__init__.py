"""Parse arguments."""
import argparse
import dataclasses

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import CELESTINE
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import TASK
from celestine.keyword.main import application
from celestine.keyword.main import language


@dataclasses.dataclass
class Argument():
    """Argument"""
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog=CELESTINE
        )

        self.parser.add_argument(
            APPLICATION,
            choices=application,
            help="Select which application to run."
        )

        self.parser.add_argument(
            "-l, --language",
            choices=language,
            help="Choose a language.",
            dest=LANGUAGE,
            metavar="language"
        )

        self.subparser = self.parser.add_subparsers(
            dest=TASK,
            required=False
        )

        self.subparser.add_parser(
            "main",
            help="The default main application."
        )


def argument():
    """argument"""
    return Argument()


def configuration(configuration):
    """configuration"""
    return configuration
