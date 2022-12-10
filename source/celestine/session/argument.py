""""""

from celestine.session.attribute import Attribute
from celestine.session import attribute as attack
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

HELP = "help"
CHOICES = "choices"


def get_attribute(
    language: types.ModuleType
) -> typing.Dict[str, Attribute]:
    """"""

    return {
        INTERFACE: attack.Override(
            load.argument_default(INTERFACE),
            language.ARGUMENT_INTERFACE_HELP,
            load.argument(INTERFACE),
        ),
        LANGUAGE: attack.Override(
            EN,
            language.ARGUMENT_LANGUAGE_HELP,
            load.argument(LANGUAGE),
        ),
        APPLICATION: attack.Positional(
            load.argument_default(APPLICATION),
            "Choose an applicanion. They have more option.",
            load.argument(APPLICATION),
        ),
        MAIN: attack.Positional(
            MAIN,
            "Choose an applicanion. They have more option.",
            [MAIN],
        ),
    }


""""""

# dataclass(frozen=True)
# field(default_factory())
# __post_init_

# fields(class_or_instance) or asdict
# metadata


@dataclasses.dataclass
class FinalHippo():
    """"""
    application: str
    interface: str
    languager: str
    main: str = dataclasses.field(
        default="main",
        metadata={
            HELP: "language.ARGUMENT_LANGUAGE_HELP",
            CHOICES: [MAIN]
        }
    )


class Hippo():
    """"""
    application: str
    interface: str
    language: str
    main: str

    @staticmethod
    def dictionary(
        language: types.ModuleType,
    ) -> typing.Dict[str, Attribute]:
        """"""

        return {
            INTERFACE: attack.Override(
                load.argument_default(INTERFACE),
                language.ARGUMENT_INTERFACE_HELP,
                load.argument(INTERFACE),
            ),
            LANGUAGE: attack.Override(
                EN,
                language.ARGUMENT_LANGUAGE_HELP,
                load.argument(LANGUAGE),
            ),
            APPLICATION: attack.Positional(
                load.argument_default(APPLICATION),
                "Choose an applicanion. They have more option.",
                load.argument(APPLICATION),
            ),
            MAIN: attack.Positional(
                MAIN,
                "Choose an applicanion. They have more option.",
                [MAIN],
            ),
        }


class Argument():
    """"""

    @ staticmethod
    def flag(
        name: str
    ) -> str:
        """name = -n"""

        iterable = (HYPHEN_MINUS, name[0])
        return str().join(iterable)

    @ staticmethod
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

        # (application, language) = self.essential(args, exit_on_error)

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

        # ignore above for now
        self.args = args
        self.application = application
        self.language = language
        self.configuration = configuration

    def __enter__(self):

        module = load.module(APPLICATION, self.application)
        special = Hippo
        special_dict = special.dictionary(self.language)
        self.feed_the_parser(special_dict)

        magic = module.Attribute2
        magic_dict = magic.dictionary(self.language)
        self.feed_the_parser(magic_dict)

        parse_args = self.parser.parse_args(self.args)

        self.attribute = self.do_work(
            special,
            special_dict,
            parse_args,
            self.configuration,
            CELESTINE,
        )

        self.new_attribute = self.do_work(
            magic,
            magic_dict,
            parse_args,
            self.configuration,
            self.application,
        )

        # combine this with attribute

        self.configuration.save()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def do_work(
        self,
        attribute_class,
        dictionary,
        parse_args,
        configuration,
        application
    ):
        """
        override the values in dictionary
        """

        attribute = attribute_class()
        for (name, fallback) in dictionary.items():
            override = getattr(parse_args, name, NONE)
            database = configuration.get(application, name)
            value = override or database or fallback.default
            setattr(attribute, name, value)
            if parse_args.configuration:
                configuration.set(application, name, override)

        return attribute

    def feed_the_parser(self, dictionary):
        """"""

        for (name, cats) in dictionary.items():

            # might be able to call this directly from class
            match type(cats):
                case attack.Optional:
                    self.optional.add_argument(
                        self.flag(name),
                        self.name(name),
                        help=cats.description,
                    )
                case attack.Override:
                    self.override.add_argument(
                        self.flag(name),
                        self.name(name),
                        choices=cats.choice,
                        help=cats.description,
                    )
                case attack.Positional:
                    self.positional.add_argument(
                        name,
                        choices=cats.choice,
                        help=cats.description,
                        nargs=QUESTION_MARK,
                    )


"""
get the dictionary A
get the dictionary B

feed the parser A
feed the parser B

update B
update A
"""
