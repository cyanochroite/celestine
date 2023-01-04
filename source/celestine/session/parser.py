""""""

import argparse


import types
import typing


from celestine.session.argument import Argument
from celestine.session.argument import Optional
from celestine.session.argument import Override
from celestine.session.argument import Information

from celestine.session.argument import Positional


from celestine.text.unicode import NONE


from celestine.session import load

from celestine.text import CELESTINE

from celestine.session import string as stringy

from celestine.text.directory import APPLICATION
from celestine.text.directory import LANGUAGE


from celestine.session.session import Magic


from .configuration import Configuration
from .session import Dictionary
from .session import Session

from .text import CONFIGURATION


class Hippo():
    """"""

    application: types.ModuleType
    language: types.ModuleType
    attribute: Dictionary
    dictionary: typing.Dict[str, Argument]

    def __init__(
        self,
        application: types.ModuleType,
        language: types.ModuleType,
        name: str,
        *path: str,
    ):

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

    def items(
        self,
    ) -> typing.Iterable[typing.Tuple[str, Argument]]:
        """"""

        return self.dictionary.items()


def get_parser(
    argv: list[str],
    exit_on_error: bool,
    language: types.ModuleType,
    attributes: list[Hippo],
    fast: bool,
    configuration,
) -> list[Dictionary]:
    """"""

    class Error(argparse.ArgumentError):
        """Intercept help formating so translation can happen."""

        def __str__(self):
            value = stringy.parser_error(
                language.ARGUMENT_PARSER_ARGUMENT,
                self.argument_name,
                self.message,
            )
            return value

    class Formatter(argparse.HelpFormatter):
        """Intercept help formating so translation can happen."""

        def add_usage(self, usage, actions, groups, prefix=None):
            prefix = stringy.parser_formatter(
                language.ARGUMENT_PARSER_USAGE,
            )
            super().add_usage(usage, actions, groups, prefix)

    class Parser(argparse.ArgumentParser):
        """Intercept help formating so translation can happen."""

        def _check_value(self, action, value):
            try:
                super()._check_value(action, value)
            except argparse.ArgumentError as error:
                value = stringy.parser_value(
                    language.ARGUMENT_PARSER_CHOICE,
                    value,
                    language.ARGUMENT_PARSER_CHOOSE,
                    action.choices,
                )
                raise Error(action, value) from error

        def error(self, message):
            value = stringy.parser_parser_error(
                self.prog,
                language.ARGUMENT_PARSER_ERROR,
                message,
            )
            self.exit(2, value)  # TODO: check if this kills blender.
            self._print_message(value)  # unreachable code

    add_argument: Magic

    parser = Parser(
        add_help=False,
        description="(cow)",
        epilog="<moo>",
        formatter_class=Formatter,
        prog=CELESTINE,
        exit_on_error=exit_on_error,
    )

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

    for attribute in attributes:
        for (name, argument) in attribute.items():
            if not argument.argument:
                continue
            _parser = add_argument[argument]
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


def start_session(argv: list[str], exit_on_error: bool) -> Session:
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
        application = load.module(APPLICATION)
        language = load.module(LANGUAGE)

        language = load_the_fish(LANGUAGE, language)
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
            "Dull",
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
