""""""

from celestine.text.unicode import NONE

import sys
import dataclasses
import argparse
import types
import typing
import enum


from celestine.session import load

from celestine.text import CELESTINE
from celestine.text import VERSION_NUMBER

from celestine.text.directory import APPLICATION
from celestine.text.directory import INTERFACE
from celestine.text.directory import LANGUAGE

from celestine.text.session import HELP
from celestine.text.session import STORE_TRUE
from celestine.text.session import VERSION


from celestine.text.unicode import HYPHEN_MINUS
from celestine.text.unicode import QUESTION_MARK

from celestine.session.configuration import Configuration

CONFIGURATION = "configuration"

# action
EN = "en"
VIEWER = "viewer"
MAIN = "main"


""""""


""""""


class Hats(enum.Enum):
    optional = enum.auto()
    override = enum.auto()
    positional = enum.auto()


@dataclasses.dataclass
class Cats():
    """"""

    hats: Hats
    default: str
    description: str
    choice: list[str]


@dataclasses.dataclass
class Attribute():
    """"""


class Argument():
    """"""

    @staticmethod
    def flag(
        name: str
    ) -> str:
        """name = -n"""

        iterable = (HYPHEN_MINUS, name[0])
        return str().join(iterable)

    @staticmethod
    def name(
        name: str
    ) -> str:
        """name = --name"""

        iterable = (HYPHEN_MINUS, HYPHEN_MINUS, name)
        return str().join(iterable)

    def __init__(
        self,
        args: list[str],
        exit_on_error: bool
    ) -> None:
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
            self.flag(LANGUAGE),
            self.name(LANGUAGE),
        )

        (argument, _) = parser.parse_known_args(args)

        configuration = Configuration.make()

        override = argument.application
        database = configuration.get(CELESTINE, APPLICATION)
        fallback = "__init__"
        application = override or database or fallback

        override = argument.language
        database = configuration.get(CELESTINE, LANGUAGE)
        fallback = "__init__"
        language = override or database or fallback

        language = load.module_fallback(LANGUAGE, argument.language)

        #(application, language) = self.essential(args, exit_on_error)

        self.dictionary: typing.Dict[str, str] = {}
        self.parser = argparse.ArgumentParser(
            add_help=False,
            prog=CELESTINE,
            exit_on_error=exit_on_error,
        )

        # FLAGS WITH NO PARAMETER
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
            self.flag(CONFIGURATION),
            self.name(CONFIGURATION),
            action=STORE_TRUE,
            help=language.ARGUMENT_HELP_HELP,
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

        space = {
            INTERFACE: Cats(
                Hats.override,
                load.argument_default(INTERFACE),
                language.ARGUMENT_INTERFACE_HELP,
                load.argument(INTERFACE),
            ),
            LANGUAGE: Cats(
                Hats.override,
                EN,
                language.ARGUMENT_LANGUAGE_HELP,
                load.argument(LANGUAGE),
            ),
            APPLICATION: Cats(
                Hats.positional,
                load.argument_default(APPLICATION),
                "Choose an applicanion. They have more option.",
                load.argument(APPLICATION),
            ),
            MAIN: Cats(
                Hats.positional,
                MAIN,
                "Choose an applicanion. They have more option.",
                [MAIN],
            ),
        }

        special = self.feed_the_parser(space)

        attribute = load.module(APPLICATION, application).attribute

        dictionary = self.feed_the_parser(attribute)

        self.attribute = Attribute()
        self.new_attribute = Attribute()

        parse_args = self.parser.parse_args(args)
        # combine this with argument

        for (name, fallback) in special.items():

            override = getattr(parse_args, name, NONE)
            database = configuration.get(application, name)
            value = override or database or fallback
            setattr(self.new_attribute, name, value)
            if parse_args.configuration:
                configuration.set(application, name, override)

        #

        for (name, fallback) in dictionary.items():

            override = getattr(parse_args, name, NONE)
            database = configuration.get(application, name)
            value = override or database or fallback
            setattr(self.attribute, name, value)
            if parse_args.configuration:
                configuration.set(application, name, override)

        # combine this with attribute

        configuration.save()

    def do_work(self, configuration):
        """"""

        for (name, fallback) in attribute.items():
            override = getattr(parse_args, name, NONE)
            database = configuration.get(application, name)
            value = override or database or fallback
            setattr(self.attribute, name, value)
            if parse_args.configuration:
                configuration.set(application, name, override)

    def feed_the_parser(self, attribute):
        """"""

        dictionary = {}

        for (name, cats) in attribute.items():
            dictionary[name] = cats.default

            match cats.hats:
                case Hats.optional:
                    self.optional.add_argument(
                        self.flag(name),
                        self.name(name),
                        help=cats.description,
                    )
                case Hats.override:
                    self.override.add_argument(
                        self.flag(name),
                        self.name(name),
                        choices=cats.choice,
                        help=cats.description,
                    )
                case Hats.positional:
                    self.positional.add_argument(
                        name,
                        choices=cats.choice,
                        help=cats.description,
                        nargs=QUESTION_MARK,
                    )

        return dictionary
