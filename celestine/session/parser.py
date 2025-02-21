""""""

import argparse
import io
from typing import Type as TYPE

from celestine.literal import (
    APOSTROPHE,
    CELESTINE,
    COLON,
    COMMA,
    HYPHEN_MINUS,
    LEFT_PARENTHESIS,
    LINE_FEED,
    NONE,
    RIGHT_PARENTHESIS,
    SPACE,
)
from celestine.typed import (
    A,
    B,
    M,
)

from .data import Parsers


def parser(language: M, exit_on_error: B) -> argparse.ArgumentParser:
    """A basic parser with overloaded functions for text translation."""
    return _parser(language)(
        prog=CELESTINE,
        usage=None,  # Default.
        description=None,  # Default.
        epilog=None,  # Default.
        parents=[],  # Default.
        formatter_class=_help_formatter(language),
        prefix_chars=HYPHEN_MINUS,  # Default
        fromfile_prefix_chars=None,  # Default.
        argument_default=None,  # Default.
        conflict_handler=Parsers.ERROR,  # Default.
        add_help=False,
        allow_abbrev=True,  # Default.
        exit_on_error=exit_on_error,
    )


def _argument_error(_: M) -> TYPE[argparse.ArgumentError]:
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

    return ArgumentError


def _help_formatter(language: M) -> TYPE[argparse.HelpFormatter]:
    """A basic parser with overloaded functions for text translation."""

    class HelpFormatter(argparse.HelpFormatter):
        """
        Formatter for generating usage message and argument help.

        strings.

        Only the name of this class is considered a public API.
        All the methods provided by the class are considered an
        implementation detail.
        """

        def add_usage(
            self,
            usage: A,
            actions: A,
            groups: A,
            prefix: A = None,
        ):
            string = io.StringIO()
            string.write(language.SESSION_PARSER_USAGE)
            string.write(COLON)
            string.write(SPACE)

            prefix = string.getvalue()
            super().add_usage(usage, actions, groups, prefix)

    return HelpFormatter


def _parser(language: M) -> TYPE[argparse.ArgumentParser]:
    """A basic parser with overloaded functions for text translation."""

    class Parser(argparse.ArgumentParser):
        """Object for parsing command line strings into objects."""

        def error(self, message: A):
            """
            Prints a usage message and exits.

            If you override this in a subclass, it should not return.
            It should either exit or raise an exception.
            """
            string = io.StringIO()
            string.write(self.prog)
            string.write(COLON)
            string.write(SPACE)
            string.write(language.SESSION_PARSER_ERROR)
            string.write(COLON)
            string.write(SPACE)
            string.write(message)
            string.write(LINE_FEED)

            value = string.getvalue()
            self.exit(2, value)

        def parse_args(self, args: A = None, namespace: A = None):  # type: ignore[override]
            args, argv = self.parse_known_args(args, namespace)
            if argv:
                string = io.StringIO()
                string.write(language.SESSION_PARSER_UNRECOGNIZED)
                string.write(COLON)
                string.write(SPACE)
                string.write(SPACE.join(argv))
                string.write(LINE_FEED)

                value = string.getvalue()
                self.error(value)
            return args

        def _check_value(self, action: A, value: A):
            # converted value must be one of the choices (if specified)

            if not action.choices:
                return

            if len(action.choices) <= 0:
                return

            if value in action.choices:
                return

            string = io.StringIO()
            string.write(language.SESSION_PARSER_CHOICE)
            string.write(COLON)
            string.write(SPACE)
            string.write(APOSTROPHE)
            string.write(value)
            string.write(APOSTROPHE)
            string.write(SPACE)
            string.write(LEFT_PARENTHESIS)
            string.write(language.SESSION_PARSER_CHOOSE)
            string.write(SPACE)

            comma_separated = [COMMA, SPACE]
            comma_separated_list = NONE.join(comma_separated)
            choice_map = map(repr, action.choices)
            choices = comma_separated_list.join(choice_map)
            string.write(choices)

            string.write(RIGHT_PARENTHESIS)

            message = string.getvalue()
            raise _argument_error(language)(action, message)

    return Parser
