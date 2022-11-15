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

from celestine.keyword.all import VERSION_NUMBER
from celestine.keyword.language import code
from celestine.keyword.language import EN
from celestine.keyword.unicode import HYPHEN_MINUS

from celestine.session import load


def flag(name):
    iterable = (HYPHEN_MINUS, name[:1])
    return str().join(iterable)


def name(name):
    iterable = (HYPHEN_MINUS, HYPHEN_MINUS, name)
    return str().join(iterable)


@dataclasses.dataclass
class Argument():
    def __init__(self, exit_on_error, language):
        self.parser = argparse.ArgumentParser(
            add_help=False,
            prog=CELESTINE,  # subparsers might change the program name?
            exit_on_error=exit_on_error,
        )

        self.parser.add_argument(
            APPLICATION,
            choices=load.argument(APPLICATION),
        )

        information = self.parser.add_argument_group(
            title=language.ARGUMENT_INFORMATION_TITLE,
            description=language.ARGUMENT_INFORMATION_DESCRIPTION,
        )

        information.add_argument(
            flag(HELP),
            name(HELP),
            action=HELP,
            help=language.ARGUMENT_HELP_HELP,
        )

        information.add_argument(
            flag(VERSION),
            name(VERSION),
            action=VERSION,
            help=language.ARGUMENT_VERSION_HELP,
            version=VERSION_NUMBER,
        )

        override = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE,
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION,
        )

        override.add_argument(
            flag(INTERFACE),
            name(INTERFACE),
            choices=load.argument(INTERFACE),
            help=language.ARGUMENT_INTERFACE_HELP,
        )

        override.add_argument(
            flag(LANGUAGE),
            name(LANGUAGE),
            choices=load.argument(LANGUAGE),
            help=language.ARGUMENT_LANGUAGE_HELP,
        )

        override.add_argument(
            flag(PYTHON),
            name(PYTHON),
            choices=load.argument(PYTHON),
            help=language.ARGUMENT_PYTHON_HELP,
        )

        # Skip remaining for now. Might move. Needs translation.

        self.subparser = self.parser.add_subparsers(
            dest=TASK,
            required=False,
        )

        self.main = self.subparser.add_parser(
            "main",
            help="The default main application.",
        )


DEFAULT = "default"


def default(argument, attribute):
    choice = getattr(argument, attribute, None)
    choices = load.argument(attribute),

    if choice in choices:
        value = load.module(attribute, choice)
    else:
        value = load.module(DEFAULT, attribute)

    setattr(argument, attribute, value)


def fast_pass(args, exit_on_error):
    parser = argparse.ArgumentParser(
        add_help=False,
        exit_on_error=exit_on_error,
        prog="FAKE NEWS"
    )
    parser.add_argument(
        flag(LANGUAGE),
        name(LANGUAGE),
        # choices=load.argument(LANGUAGE),
        # default=EN,
    )

#    parser = ArgumentParser(add_help=False, exit_on_error=exit_on_error)
#    parser.add_argument(flag(LANGUAGE), name(LANGUAGE))

    (argument, _) = parser.parse_known_args(args)

    default(argument, LANGUAGE)
    default(argument, APPLICATION)

    return argument
