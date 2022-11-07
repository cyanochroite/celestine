import argparse
import dataclasses


from celestine.keyword.all import APPLICATION
from celestine.keyword.all import CELESTINE
from celestine.keyword.all import TASK
from celestine.keyword.all import application

from celestine.keyword.language import LANGUAGE
from celestine.keyword.language import language

from celestine.keyword.unicode import HYPHEN_MINUS


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
            APPLICATION,
            choices=application,
            help="Select which application to run.",
        )

        self.parser.add_argument(
            self.flag(LANGUAGE),
            self.name(LANGUAGE),
            choices=language,
            help="""
                The EU has 24 official languages: Bulgarian, Croatian, Czech,
                Danish, Dutch, English, Estonian, Finnish, French, German,
                Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese,
                Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish and
                Swedish.
            """,
            metavar=self.meta(LANGUAGE),
            type=str.lower,
        )

        self.subparser = self.parser.add_subparsers(
            dest=TASK,
            required=False,
        )

        self.main = self.subparser.add_parser(
            "main",
            help="The default main application.",
        )
