""""""

import argparse
import types
import typing

from celestine.session import load

from celestine.text import CELESTINE
from celestine.text import VERSION_NUMBER

from celestine.text.directory import APPLICATION
from celestine.text.directory import DEFAULT
from celestine.text.directory import INTERFACE
from celestine.text.directory import LANGUAGE
from celestine.text.directory import PYTHON

from celestine.text.session import HELP
from celestine.text.session import TASK
from celestine.text.session import VERSION


from celestine.text.unicode import HYPHEN_MINUS
from celestine.text.unicode import QUESTION_MARK


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

        default_application = load.argument_default(APPLICATION)
        default_language = load.argument_default(LANGUAGE)

        application = argument.application or default_application
        language = argument.language or default_language
        print("language default is weird")

        language = load.module(LANGUAGE, language)

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

        self.information = self.parser.add_argument_group(
            title=language.ARGUMENT_INFORMATION_TITLE,
            description=language.ARGUMENT_INFORMATION_DESCRIPTION,
        )

        self.override = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE,
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION,
        )

        self.positional = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
            description =language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
        )

        self.optional = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
            description =language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
        )

        self.information.add_argument(
            self.flag(HELP),
            self.name(HELP),
            action=HELP,
            help=language.ARGUMENT_HELP_HELP,
        )

        self.information.add_argument(
            self.flag(VERSION),
            self.name(VERSION),
            action=VERSION,
            help=language.ARGUMENT_VERSION_HELP,
            version=VERSION_NUMBER,
        )

        self.override.add_argument(
            self.flag(INTERFACE),
            self.name(INTERFACE),
            choices=load.argument(INTERFACE),
            help=language.ARGUMENT_INTERFACE_HELP,
        )

        self.override.add_argument(
            self.flag(LANGUAGE),
            self.name(LANGUAGE),
            choices=load.argument(LANGUAGE),
            help=language.ARGUMENT_LANGUAGE_HELP,
        )

        self.override.add_argument(
            self.flag(PYTHON),
            self.name(PYTHON),
            choices=load.argument(PYTHON),
            help=language.ARGUMENT_PYTHON_HELP,
        )

        self.add_positional(
            APPLICATION,
            "Choose an applicanion. They have more option.",
            load.argument_default(APPLICATION),
            load.argument(APPLICATION),
        )

        self.add_positional(
            TASK,
            "Choose an applicanion. They have more option.",
            "main",
            load.argument(APPLICATION, application),
        )

        load.module(APPLICATION, application).add_argument(self)

    def add_positional(
        self,
        name: str,
        description: str,
        default: str,
        choice: list[str],
    ) -> None:
        """"""

        self.dictionary[name] = default

        self.positional.add_argument(
            name,
            choices=choice,
            help=description,
            nargs=QUESTION_MARK,
        )

    def add_optional(
        self,
        name: str,
        description: str,
        default: str,
    ) -> None:
        """"""

        self.dictionary[name] = default

        self.optional.add_argument(
            self.flag(name),
            self.name(name),
            help=description,
        )

    def get_argument(
        self,
    ) -> typing.Dict[str, str]:
        """"""

        return self.dictionary
