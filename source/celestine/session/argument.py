""""""

import argparse
import types
import typing

from celestine.text.all import APPLICATION
from celestine.text.all import CELESTINE
from celestine.text.all import DEFAULT
from celestine.text.all import HELP
from celestine.text.all import INTERFACE
from celestine.text.all import LANGUAGE
from celestine.text.all import PYTHON
from celestine.text.all import VERSION
from celestine.text.all import VERSION_NUMBER

from celestine.text.unicode import HYPHEN_MINUS
from celestine.text.unicode import QUESTION_MARK

from celestine.session import load

TASK = "task"


class Argument():
    """"""

    @staticmethod
    def flag(
        name: str
    ) -> str:
        """"""

        iterable = (HYPHEN_MINUS, name[:1])
        return str().join(iterable)

    @staticmethod
    def name(
        name: str
    ) -> str:
        """"""

        iterable = (HYPHEN_MINUS, HYPHEN_MINUS, name)
        return str().join(iterable)

    @staticmethod
    def default(
        name: str,
        value: str
    ) -> types.ModuleType:
        """"""

        values = load.argument(name)

        if value in values:
            module = load.module(name, value)
        else:
            module = load.module(DEFAULT, name)

        return module

    @classmethod
    def region(
        cls,
        args: list[str],
        exit_on_error: bool
    ) -> typing.Tuple[str, types.ModuleType]:
        """"""

        parser = argparse.ArgumentParser(
            add_help=False,
            exit_on_error=exit_on_error,
        )

        parser.add_argument(
            APPLICATION,
            nargs=QUESTION_MARK,
        )

        parser.add_argument(
            cls.flag(LANGUAGE),
            cls.name(LANGUAGE),
        )

        (argument, _) = parser.parse_known_args(args)

        application = str(argument.application)
        language = cls.default(LANGUAGE, argument.language)

        return (application, language)

    def __init__(
        self,
        args: list[str],
        exit_on_error: bool
    ) -> None:
        """"""

        self.dictionary: typing.Dict[str, str] = {}

        (application, language) = self.region(args, exit_on_error)

        self.parser = argparse.ArgumentParser(
            add_help=False,
            prog=CELESTINE,
            exit_on_error=exit_on_error,
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

        load.module(APPLICATION, application).add_argument(self)

        self.subparser = self.parser.add_argument(
            APPLICATION,
            choices=load.argument(APPLICATION),
            help="Choose an applicanion. They have more option.",
            nargs=QUESTION_MARK,
        )

        self.subparser = self.parser.add_argument(
            TASK,
            choices=load.argument(APPLICATION, application),
            help="Choose an applicanion. They have more option.",
            nargs=QUESTION_MARK,
        )

    def add_argument(
        self,
        default: str,
        description: str,
        name: str,
        required: bool,
    ) -> None:
        """"""

        self.dictionary[name] = default

        if required:
            self.parser.add_argument(
                name,
                help=description,
            )
        else:
            self.parser.add_argument(
                self.flag(name),
                self.name(name),
                help=description,
            )
