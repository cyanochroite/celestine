import argparse

from celestine.keyword.all import APPLICATION
from celestine.keyword.all import CELESTINE
from celestine.keyword.all import DEFAULT
from celestine.keyword.all import HELP
from celestine.keyword.all import INTERFACE
from celestine.keyword.all import LANGUAGE
from celestine.keyword.all import PYTHON
from celestine.keyword.all import VERSION
from celestine.keyword.all import VERSION_NUMBER

from celestine.keyword.unicode import HYPHEN_MINUS

from celestine.session import load

TASK = "task"


class Argument():
    def flag(self, name):
        iterable = (HYPHEN_MINUS, name[:1])
        return str().join(iterable)

    def name(self, name):
        iterable = (HYPHEN_MINUS, HYPHEN_MINUS, name)
        return str().join(iterable)

    def region(self, args, exit_on_error):

        parser = argparse.ArgumentParser(
            add_help=False,
            exit_on_error=exit_on_error,
        )

        parser.add_argument(
            self.flag(LANGUAGE),
            self.name(LANGUAGE),
        )

        (argument, _) = parser.parse_known_args(args)

        language = argument.language
        languages = load.argument(LANGUAGE)

        if language in languages:
            module = load.module(LANGUAGE, language)
        else:
            module = load.module(DEFAULT, LANGUAGE)

        return module

    def __init__(self, args, exit_on_error):
        language = self.region(args, exit_on_error)

        self.parser = argparse.ArgumentParser(
            add_help=False,
            prog=CELESTINE,
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
            self.flag(HELP),
            self.name(HELP),
            action=HELP,
            help=language.ARGUMENT_HELP_HELP,
        )

        information.add_argument(
            self.flag(VERSION),
            self.name(VERSION),
            action=VERSION,
            help=language.ARGUMENT_VERSION_HELP,
            version=VERSION_NUMBER,
        )

        override = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE,
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION,
        )

        override.add_argument(
            self.flag(INTERFACE),
            self.name(INTERFACE),
            choices=load.argument(INTERFACE),
            help=language.ARGUMENT_INTERFACE_HELP,
        )

        override.add_argument(
            self.flag(LANGUAGE),
            self.name(LANGUAGE),
            choices=load.argument(LANGUAGE),
            help=language.ARGUMENT_LANGUAGE_HELP,
        )

        override.add_argument(
            self.flag(PYTHON),
            self.name(PYTHON),
            choices=load.argument(PYTHON),
            help=language.ARGUMENT_PYTHON_HELP,
        )

        self.subparser = self.parser.add_subparsers(
            dest=TASK,
            required=False,
        )
        #  new

        applications = load.argument(APPLICATION)
        for application in applications:
            module = load.module(APPLICATION, application)
            module.argument(self)




