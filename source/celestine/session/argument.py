from argparse import ArgumentParser
import argparse
import dataclasses


from celestine.keyword.all import APPLICATION
from celestine.keyword.all import CELESTINE
from celestine.keyword.all import TASK
from celestine.keyword.all import application

from celestine.keyword.language import LANGUAGE
from celestine.keyword.language import language
from celestine.keyword.language import EN

from celestine.keyword.unicode import HYPHEN_MINUS


from celestine.keyword.language import code

APPLICATION = "application"
HELP = "help"
# help
INTERFACE = "interface"
# language
PYTHON = "python"
VERSION = "version"


def flag(name):
    iterable = (HYPHEN_MINUS, name[:1])
    return str().join(iterable)


def name(name):
    iterable = (HYPHEN_MINUS, HYPHEN_MINUS, name)
    return str().join(iterable)


@dataclasses.dataclass
class Argument():
    def __init__(self, exit_on_error, translate):
        self.parser = argparse.ArgumentParser(
            add_help=False,
            prog=CELESTINE,
            exit_on_error=exit_on_error,
        )

        self.parser.add_argument(
            flag(APPLICATION),
            name(APPLICATION),
        )

        self.parser.add_argument(
            flag(HELP),
            name(HELP),
            action=HELP,
            help="I ate a fish!",
        )

        self.parser.add_argument(
            flag(INTERFACE),
            name(INTERFACE),
        )

        self.parser.add_argument(
            flag(LANGUAGE),
            name(LANGUAGE),
            choices=code,
            default=EN,
            help=translate.LANGUAGE,
        )

        self.parser.add_argument(
            flag(PYTHON),
            name(PYTHON),
            choices=["3.7", "3.8"],
        )

        self.parser.add_argument(
            flag(VERSION),
            name(VERSION),
            action=VERSION,
            help="Go Fishing trip!",
            version="0.4.0",
        )

        self.subparser = self.parser.add_subparsers(
            dest=TASK,
            required=False,
        )

        self.main = self.subparser.add_parser(
            "main",
            help="The default main application.",
        )


def language(args, exit_on_error):
    parser = ArgumentParser(
        add_help=False,
        exit_on_error=exit_on_error,
        prog=CELESTINE,
    )
    parser.add_argument(
        flag(LANGUAGE),
        name(LANGUAGE),
        choices=code,
        default=EN,
    )
    (argument, _) = parser.parse_known_args(args)
    return argument.language
