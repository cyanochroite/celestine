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

EN = "en"
VIEWER = "viewer"


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

    @classmethod
    def essential(
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

        application = getattr(
            argument,
            APPLICATION,
            load.argument_default(APPLICATION)
        )

        application = argument.application or VIEWER
        language = load.module(LANGUAGE, argument.language or EN)

        return (application, language)

    def __init__(
        self,
        args: list[str],
        exit_on_error: bool
    ) -> None:
        """"""

        (application, language) = self.essential(args, exit_on_error)

        self.application = application
        self.dictionary: typing.Dict[str, str] = {}
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
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
        )

        self.optional = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
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

        self.add_override(
            INTERFACE,
            language.ARGUMENT_INTERFACE_HELP,
            load.argument_default(INTERFACE),
            load.argument(INTERFACE),
        )

        self.add_override(
            LANGUAGE,
            language.ARGUMENT_LANGUAGE_HELP,
            EN,
            load.argument(LANGUAGE),
        )

        self.add_override(
            PYTHON,
            language.ARGUMENT_PYTHON_HELP,
            load.argument_default(PYTHON),
            load.argument(PYTHON),
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

    def add_override(
        self,
        name: str,
        description: str,
        default: str,
        choice: list[str],
    ) -> None:
        """"""

        self.dictionary[name] = default

        self.override.add_argument(
            self.flag(name),
            self.name(name),
            choices=choice,
            help=description,
        )
