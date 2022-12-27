""""""

import argparse

import types
import typing

from celestine.session.argument import Argument
from celestine.session.argument import Optional
from celestine.session.argument import Override
from celestine.session.argument import Information
from celestine.session.argument import Name
from celestine.session.argument import Flag

from celestine.session.argument import Positional


from celestine.text.unicode import NONE


from celestine.session import load

from celestine.text import CELESTINE

from celestine.text.directory import APPLICATION
from celestine.text.directory import LANGUAGE

from celestine.session.session import Magic


from .configuration import Configuration
from .session import Dictionary
from .session import Session

from .text import CONFIGURATION
from .text import INIT


class Hippo():
    """"""

    application: str
    language: types.ModuleType
    attribute: Dictionary
    dictionary: typing.Dict[str, Argument]

    def __init__(
        self,
        application: str,
        language: types.ModuleType,
        name: str,
        *path: str,
    ):

        self.application = application
        self.language = language

        module = load.module(*path)

        session = getattr(module, name)
        self.attribute = session()
        self.dictionary = self.attribute.dictionary(self.language)

    def items(
        self,
    ) -> typing.Iterable[typing.Tuple[str, Argument]]:
        """"""

        return self.dictionary.items()


def dofilt(
    argv: list[str],
    exit_on_error: bool
) -> Dictionary:
    """"""

    add_argument: Magic

    language = load.module(LANGUAGE, INIT)

    configuration = Configuration()
    configuration.load()

    parser = argparse.ArgumentParser(
        add_help=False,
        exit_on_error=exit_on_error,
    )

    add_argument = {}
    add_argument[Name] = parser
    add_argument[Flag] = parser

    attribute = feed_the_parser(
        add_argument,
        lambda: parser.parse_known_args(argv)[0],
        configuration,
        [
            Hippo(
                CELESTINE,
                language,
                "Turbo",
                "session",
                "session",
            ),
        ],
    )

    return attribute[0]


def dostuff(
    args: list[str],
    exit_on_error: bool,
    application: str,
    language: types.ModuleType,
) -> Session:
    """"""

    add_argument: Magic

    parser = argparse.ArgumentParser(
        add_help=False,
        prog=CELESTINE,
        exit_on_error=exit_on_error,
    )

    add_argument = {}

    information = parser.add_argument_group(
        title=language.ARGUMENT_INFORMATION_TITLE,
        description=language.ARGUMENT_INFORMATION_DESCRIPTION,
    )
    optional = parser.add_argument_group(
        title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
        description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
    )
    override = parser.add_argument_group(
        title=language.ARGUMENT_OVERRIDE_TITLE,
        description=language.ARGUMENT_OVERRIDE_DESCRIPTION,
    )
    positional = parser.add_argument_group(
        title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
        description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
    )

    add_argument = {}
    add_argument[Information] = information
    add_argument[Optional] = optional
    add_argument[Override] = override
    add_argument[Positional] = positional

    configuration = Configuration()
    configuration.load()

    attribute = feed_the_parser(
        add_argument,
        lambda: parser.parse_args(args),
        configuration,
        [
            Hippo(
                application,
                language,
                "Session",
                "session",
                "session",
            ),
            Hippo(
                application,
                language,
                "Session",
                APPLICATION,
                application,
            ),
            Hippo(
                application,
                language,
                "Dull",
                "session",
                "session",
            ),
        ],
    )

    configuration.save()

    session = attribute[0]
    session.attribute = attribute[1]

    return session


def feed_the_parser(
    add_argument: Magic,
    calling,
    configuration,
    attributes: list[Hippo],
) -> list[Dictionary]:
    """"""

    for attribute in attributes:
        for (name, argument) in attribute.items():
            parser = add_argument[argument]
            args = argument.key(name)
            kwargs = argument.dictionary()

            parser.add_argument(*args, **kwargs)

    args = calling()

    for attribute in attributes:
        for (name, argument) in attribute.items():
            if not argument.use:
                continue
            override = getattr(args, name, NONE)
            database = configuration.get(attribute.application, name)
            value = override or database or argument.fallback
            setattr(attribute.attribute, name, value)
            if getattr(args, CONFIGURATION, NONE):
                configuration.set(attribute.application, name, override)

    return [attribute.attribute for attribute in attributes]


def start_session(argv: list[str], exit_on_error: bool) -> Session:
    """"""
    turbo = dofilt(argv, exit_on_error)
    application = turbo.application
    language = turbo.language

    session = dostuff(argv, exit_on_error, application, language)
    return session
