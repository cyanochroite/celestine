import sys
import configparser
import configparser
import argparse
import dataclasses


from celestine.keyword.all import APPLICATION
from celestine.keyword.all import LANGUAGE
from celestine.keyword.all import TASK

from celestine.keyword.all import CELESTINE



from celestine.core import load

from celestine.keyword.all import CELESTINE
from celestine.keyword.all import CONFIGURATION
from celestine.keyword.all import WRITE
from celestine.keyword.all import UTF_8


from celestine.keyword.all import APPLICATION
from celestine.keyword.all import CELESTINE
from celestine.keyword.all import LANGUAGE
from celestine.keyword.all import TASK
from celestine.keyword.all import application
from celestine.keyword.all import language


PYTHON = "python"

PYTHON_3_6 = "python_3_6"
PYTHON_3_7 = "python_3_7"
PYTHON_3_8 = "python_3_8"
PYTHON_3_9 = "python_3_9"
PYTHON_3_10 = "python_3_10"
PYTHON_3_11 = "python_3_11"


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

