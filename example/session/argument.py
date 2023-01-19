import argparse
import dataclasses


from celestine.keyword.all import APPLICATION
from celestine.keyword.all import CELESTINE
from celestine.keyword.all import TASK
from celestine.keyword.all import application
from celestine.keyword.all import language


@dataclasses.dataclass
class Argument():
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
            "-l",
            "--language",
            choices=language,
            help="""
                The EU has 24 official languages: Bulgarian, Croatian, Czech,
                Danish, Dutch, English, Estonian, Finnish, French, German,
                Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese,
                Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish and
                Swedish.
            """,
            metavar="LANGUAGE",
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
