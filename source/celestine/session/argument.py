import argparse
import dataclasses

from celestine.keyword.all import APPLICATION
from celestine.keyword.all import CELESTINE
from celestine.keyword.all import HELP
from celestine.keyword.all import INTERFACE
from celestine.keyword.all import LANGUAGE
from celestine.keyword.all import PYTHON
from celestine.keyword.all import TASK
from celestine.keyword.all import VERSION

from celestine.keyword.language import code
from celestine.keyword.unicode import HYPHEN_MINUS
from celestine.keyword.language import EN

from celestine.session import load


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
            choices=load.argument(APPLICATION),
        )

        information = self.parser.add_argument_group(
            title="Information",
            description="""
            Including these will end the program to display information.
            """
        )

        information.add_argument(
            flag(HELP),
            name(HELP),
            action=HELP,
            help="I ate a fish!",
        )

        information.add_argument(
            flag(VERSION),
            name(VERSION),
            action=VERSION,
            help="Go Fishing trip!",
            version="0.4.0",
        )

        override = self.parser.add_argument_group(
            title="Override",
            description="""
            Celestine will try to guess the best settings to use.
            You can request to use these values instead.
            """
        )

        override.add_argument(
            flag(INTERFACE),
            name(INTERFACE),
            choices=load.argument(INTERFACE),
        )

        override.add_argument(
            flag(LANGUAGE),
            name(LANGUAGE),
            choices=load.argument(LANGUAGE),
            default=EN,
            help=translate.LANGUAGE,
        )

        override.add_argument(
            flag(PYTHON),
            name(PYTHON),
            choices=load.argument(PYTHON),
        )

        ###

        self.subparser = self.parser.add_subparsers(
            dest=TASK,
            required=False,
        )

        self.main = self.subparser.add_parser(
            "main",
            help="The default main application.",
        )


def language(args, exit_on_error):
    parser = argparse.ArgumentParser(
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
