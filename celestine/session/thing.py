
import io

import io

from celestine.typed import (
    L,
    S,
)
from celestine.unicode import (
    APOSTROPHE,
    COLON,
    COMMA,
    LEFT_PARENTHESIS,
    LINE_FEED,
    NONE,
    RIGHT_PARENTHESIS,
    SPACE,
)


import argparse
import locale
from argparse import ArgumentParser as AP
from typing import TypeAlias as TA

from celestine import load
from celestine.session import word
from celestine.session.argument import (
    Application,
    Customization,
    InformationConfiguration,
    InformationHelp,
    InformationVersion,
    Optional,
    Positional,
)
from celestine.text import CELESTINE
from celestine.text.directory import (
    APPLICATION,
    INTERFACE,
    LANGUAGE,
)
from celestine.typed import (
    MT,
    TY,
    A,
    B,
    D,
    L,
    N,
    S,
)
from celestine.unicode import NONE

from .configuration import Configuration
from .session import (
    Dictionary,
    Session,
)
from .text import CONFIGURATION

INIT = "__init__"


# ADI: typing.TypeAlias = typing.Iterable[typing.Tuple[str, Argument]]

# APD: TA = D[U[Argument, T[Argument]], U[AP, AG]]
APD: TA = D[A, A]



def new(language: MT, exit_on_error: B) -> AP:
    """A basic parser with overloaded functions for text translation."""


    class ArgumentError(argparse.ArgumentError):
        """
        An error from creating or using an argument.

        The string value of this exception is the message,
        augmented with information about the argument that caused it.
        """

        def __str__(self):
            string = io.StringIO()
            if self.argument_name is not None:
                string.write(self.argument_name)
                string.write(SPACE)
                string.write(self.argument_name)
                string.write(COLON)
                string.write(SPACE)
            string.write(self.message)
            value = string.getvalue()
            return value


    class HelpFormatter(argparse.HelpFormatter):
        """
        Formatter for generating usage message and argument help strings.

        Only the name of this class is considered a public API.
        All the methods provided by the class are considered an
        implementation detail.
        """

        def add_usage(self, usage, actions, groups):
            string = io.StringIO()
            string.write(language.ARGUMENT_PARSER_USAGE)
            string.write(COLON)
            string.write(SPACE)

            prefix = string.getvalue()
            super().add_usage(usage, actions, groups, prefix)


    class Parser(argparse.ArgumentParser):
        """Object for parsing command line strings into objects."""

        def error(self, message):
            """
            Prints a usage message and exits.

            If you override this in a subclass, it should not return.
            It should either exit or raise an exception.
            """

            string = io.StringIO()
            string.write(self.prog)
            string.write(COLON)
            string.write(SPACE)
            string.write(language.ARGUMENT_PARSER_ERROR)
            string.write(COLON)
            string.write(SPACE)
            string.write(message)
            string.write(LINE_FEED)

            value = string.getvalue()
            self.exit(2, value)


        def _check_value(self, action, value):
            # converted value must be one of the choices (if specified)
            exists = action.choices is not None
            valid = len(action.choices) > 0
            missing = value not in action.choices
            if exists and valid and missing:
                string = io.StringIO()
                string.write(language.ARGUMENT_PARSER_CHOICE)
                string.write(COLON)
                string.write(SPACE)
                string.write(APOSTROPHE)
                string.write(value)
                string.write(APOSTROPHE)
                string.write(SPACE)
                string.write(LEFT_PARENTHESIS)
                string.write(language.ARGUMENT_PARSER_CHOOSE)
                string.write(SPACE)

                comma_separated = [COMMA, SPACE]
                comma_separated_list = NONE.join(comma_separated)
                choice_map = map(repr, action.choices)
                choices = comma_separated_list.join(choice_map)
                string.write(choices)

                string.write(RIGHT_PARENTHESIS)

                message = string.getvalue()
                raise ArgumentError(action, message)


    parser = Parser(
        add_help=False,
        # description="(cow)",
        # epilog="<moo>",
        formatter_class=HelpFormatter,
        prog=CELESTINE,
        exit_on_error=exit_on_error,
    )

    return parser