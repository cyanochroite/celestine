""""""

import argparse

from typing import TypeAlias as TA
from typing import Dict as D
from typing import Union as U
from typing import Type as T
from argparse import _ArgumentGroup as AG

from celestine.session.argument import InformationConfiguration
from celestine.session.argument import InformationHelp
from celestine.session.argument import InformationVersion


from celestine.text.directory import LANGUAGE
from celestine.text.directory import APPLICATION
from celestine.text.directory import INTERFACE

from celestine.session import word
from celestine.text import CELESTINE
from celestine.session import load
from celestine.text.unicode import NONE
from celestine.session.argument import Positional
from celestine.session.argument import Information
from celestine.session.argument import Application
from celestine.session.argument import Argument
from celestine.session.argument import Customization

# from celestine.session.type import string


from .text import CONFIGURATION
from .session import Session
from .session import Dictionary
from .configuration import Configuration

from .type import AD
from .type import ADI
from .type import AP
# from .type import APD
from .type import AT
from .type import B
from .type import I
from .type import S
from .type import SL
from .type import MT
from .type import N

APD: TA = D[U[Argument, T[Argument]], U[AP, AG]]


class Hippo():
    """"""

    application: MT
    language: MT
    attribute: Dictionary
    dictionary: AD

    def __init__(self, application: MT, language: MT, name: S, *path: S) -> N:

        self.application = application
        self.language = language

        try:
            module = load.module(*path)
        except TypeError:
            module = self.application

        session = getattr(module, name)
        self.attribute = session()
        dictionary = self.attribute.dictionary
        self.dictionary = dictionary(application, language)

    def items(self) -> ADI:
        """"""

        return self.dictionary.items()


def make_parser(language: MT, exit_on_error: B) -> AP:
    """"""

    class Error(argparse.ArgumentError):
        """Intercept help formating so translation can happen."""

        def __str__(self):
            value = word.parser_error(
                language.ARGUMENT_PARSER_ARGUMENT,
                self.argument_name,
                self.message,
            )
            return value

    class Formatter(argparse.HelpFormatter):
        """Intercept help formating so translation can happen."""

        def add_usage(self, usage, actions, groups, prefix=None):
            prefix = word.parser_formatter(
                language.ARGUMENT_PARSER_USAGE,
            )
            super().add_usage(usage, actions, groups, prefix)

    class Parser(argparse.ArgumentParser):
        """Intercept help formating so translation can happen."""

        def _check_value(self, action, value):
            try:
                super()._check_value(action, value)
            except argparse.ArgumentError as error:
                value = word.parser_value(
                    language.ARGUMENT_PARSER_CHOICE,
                    value,
                    language.ARGUMENT_PARSER_CHOOSE,
                    action.choices,
                )
                raise Error(action, value) from error

        def error(self, message):
            value = word.parser_parser_error(
                self.prog,
                language.ARGUMENT_PARSER_ERROR,
                message,
            )
            self.exit(2, value)  # TODO: check if this kills blender.
            self._print_message(value)  # unreachable code

    parser = Parser(
        add_help=False,
        description="(cow)",
        epilog="<moo>",
        formatter_class=Formatter,
        prog=CELESTINE,
        exit_on_error=exit_on_error,
    )

    return parser


def make_arguments(language: MT, parser: AP) -> APD:
    """"""

    application = parser.add_argument_group(
        title=language.ARGUMENT_APPLICATION_TITLE,
        description=language.ARGUMENT_APPLICATION_DESCRIPTION,
    )
    """your program stuff goes here. usefull, noone"""

    customization = parser.add_argument_group(
        title=language.ARGUMENT_CUSTOMIZATION_TITLE,
        description=language.ARGUMENT_CUSTOMIZATION_DESCRIPTION,
    )
    """all applications use these. usefull, everone"""

    information = parser.add_argument_group(
        title=language.ARGUMENT_INFORMATION_TITLE,
        description=language.ARGUMENT_INFORMATION_DESCRIPTION,
    )
    """displays information then exits. useless, noone"""

    modification = parser.add_argument_group(
        title=language.ARGUMENT_MODIFICATION_TITLE,
        description=language.ARGUMENT_MODIFICATION_DESCRIPTION,
    )
    """all applications use these. useless, everyone"""

    arguments: APD = {}
    arguments[Application] = application
    arguments[Customization] = customization

    arguments[Information] = information
    arguments[InformationConfiguration] = information
    arguments[InformationHelp] = information
    arguments[InformationVersion] = information

    arguments[Positional] = modification

    return arguments


def add_argument(arguments, attributes):
    """"""
    for attribute in attributes:
        for (name, argument) in attribute.items():
            if not argument.argument:
                continue
            parser = arguments[argument]
            args = argument.key(name)
            kwargs = argument.dictionary()
            parser.add_argument(*args, **kwargs)


def get_parser(argv: SL, exit_on_error: B, language: MT,
               attributes: list[Hippo], fast: B,
               configuration: Configuration) -> list[Dictionary]:
    """"""

    parser = make_parser(language, exit_on_error)

    arguments = make_arguments(language, parser)

    # add_argument(arguments, attributes)

    for attribute in attributes:
        for (name, argument) in attribute.items():
            if not argument.argument:
                continue
            _parser = arguments[argument]
            args = argument.key(name)
            kwargs = argument.dictionary()
            _parser.add_argument(*args, **kwargs)

    if fast:
        args = parser.parse_known_args(argv)[0]
    else:
        args = parser.parse_args(argv)

    for attribute in attributes:
        for (name, argument) in attribute.items():
            if not argument.attribute:
                continue
            override = getattr(args, name, NONE)
            database = configuration.get(attribute.application, name)
            value = override or database or argument.fallback
            setattr(attribute.attribute, name, value)
            if getattr(args, CONFIGURATION, NONE):
                configuration.set(attribute.application, name, override)

    attribute = [attribute.attribute for attribute in attributes]

    return attribute


def start_session(argv: SL, exit_on_error: B) -> Session:
    """"""
    configuration = Configuration()
    configuration.load()

    def load_the_fish(name, value):
        hippo = [
            Hippo(
                load.module(),
                language,
                name.capitalize(),
                "session",
                "session",
            ),
        ]
        parser = get_parser(
            argv,
            exit_on_error,
            language,
            hippo,
            True,
            configuration,
        )[0]
        thing = getattr(parser, name, value)
        return thing

    try:
        language = load.module(LANGUAGE)
        interface = load.module(INTERFACE)
        application = load.module(APPLICATION)

        language = load_the_fish(LANGUAGE, language)
        interface = load_the_fish(INTERFACE, interface)
        application = load_the_fish(APPLICATION, application)

    except ModuleNotFoundError as error:
        raise RuntimeError("Missing __init__ file.") from error

    hippos = [
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
            "Information",
            "session",
            "session",
        ),
    ]
    attribute = get_parser(
        argv,
        exit_on_error,
        language,
        hippos,
        True,
        configuration,
    )

    session = attribute[0]
    session.attribute = attribute[1]

    configuration.save()

    return session


"""
importer notes.

language.py is all you need for 1 language.
language/__init__.py can be used instead.

Not recomended to use both. However, note that
language/__init__.py takes priority over language.py

Must have at least one of these.
Recomend using directory version so you can add more languages.
Error messages will assume this version.

if you have more then 1 language you must use language/__init__.py
"""


"""
configuration information will show your saved stuff
"""
