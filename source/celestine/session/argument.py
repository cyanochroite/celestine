import argparse
import dataclasses


from celestine.keyword.all import APPLICATION
from celestine.keyword.all import CELESTINE
from celestine.keyword.all import TASK
from celestine.keyword.all import application

from celestine.keyword.language import LANGUAGE
from celestine.keyword.language import language

from celestine.keyword.unicode import HYPHEN_MINUS


from celestine.languages import en as translate  # FIX

from celestine.keyword.language import code

DIRECTORY = "directory"
# help
INTERFACE = "interface"
# language
PYTHON = "python"


@dataclasses.dataclass
class Argument():
    def flag(self, name):
        iterable = (HYPHEN_MINUS, name[:1])
        return str().join(iterable)

    def name(self, name):
        iterable = (HYPHEN_MINUS, HYPHEN_MINUS, name)
        return str().join(iterable)

    def meta(self, name):
        return name.upper()

    def __init__(self, exit_on_error):
        self.parser = argparse.ArgumentParser(
            prog=CELESTINE,
            exit_on_error=exit_on_error,
        )

        self.parser.add_argument(
            LANGUAGE,
            choices=code,
            help=translate.LANGUAGE,
        )

        self.parser.add_argument(
            self.flag(DIRECTORY),
            self.name(DIRECTORY),
            metavar=self.meta(DIRECTORY),
        )

        self.parser.add_argument(
            self.flag(INTERFACE),
            self.name(INTERFACE),
            metavar=self.meta(INTERFACE),
        )
        self.parser.add_argument(
            self.flag(PYTHON),
            self.name(PYTHON),
            metavar=self.meta(PYTHON),
        )

        self.subparser = self.parser.add_subparsers(
            dest=TASK,
            required=False,
        )

        self.main = self.subparser.add_parser(
            "main",
            help="The default main application.",
        )
