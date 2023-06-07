""""""

import argparse
import io
from typing import TypeAlias as TA

from celestine import load
from celestine.data import CELESTINE
from celestine.session.argument import (
    Application,
    Customization,
    InformationConfiguration,
    InformationHelp,
    InformationVersion,
    Optional,
    Positional,
)
from celestine.session.configuration import Configuration
from celestine.session.data import CONFIGURATION
from celestine.session.session import Session as SessionParse
from celestine.typed import (
    MT,
    TA,
    A,
    B,
    D,
    L,
    N,
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

from . import default
from .configuration import Configuration
from .data import SESSION
from .session import Session as SessionParse

INIT = "__init__"

# ADI: typing.TypeAlias = typing.Iterable[typing.Tuple[str, Argument]]
# APD: TA = D[U[Argument, T[Argument]], U[AP, AG]]
APD: TA = D[A, A]

AP: TA = argparse.ArgumentParser


class Core:
    """"""

    application: MT
    interface: MT
    language: MT

    def __init__(self, application: S, interface: S, language: S) -> N:
        """"""

        self.application = application
        self.interface = interface
        self.language = language

    def __setattr__(self, name, value):
        module = load.module(name, value)
        module.name = value
        super().__setattr__(name, module)


def make_parser(language: MT, exit_on_error: B) -> AP:
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
        Formatter for generating usage message and argument help.

        strings.

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

        def parse_args(self, args=None, namespace=None):
            args, argv = self.parse_known_args(args, namespace)
            if argv:
                string = io.StringIO()
                string.write("unrecognized arguments")
                string.write(COLON)
                string.write(SPACE)
                string.write(SPACE.join(argv))
                string.write(LINE_FEED)

                value = string.getvalue()
                self.error(value)
            return args

        def _check_value(self, action, value):
            # converted value must be one of the choices (if specified)

            if not action.choices:
                return

            if len(action.choices) <= 0:
                return

            if value in action.choices:
                return

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


class Magic:
    def get_parser(self, attributes: L[SessionParse], known: B) -> N:
        """Attributes is modified in place."""

        self.parser = make_parser(
            self.core.language, self.exit_on_error
        )

        self._add_argument(attributes)

        self._parse_args(known)

        self._add_attribute(attributes)

    def parse(self, name) -> MT:
        """Quickly parse important attributes."""
        method = load.method(name.capitalize(), SESSION, SESSION)
        self.get_parser([method], True)
        setattr(self.core, name, getattr(method, name))

    ###

    def _make_argument_group(self) -> APD:
        """"""

        language = self.core.language

        application = self.parser.add_argument_group(
            title=language.ARGUMENT_APPLICATION_TITLE,
            description=language.ARGUMENT_APPLICATION_DESCRIPTION,
        )
        # Your program stuff goes here: usefull, noone.

        customization = self.parser.add_argument_group(
            title=language.ARGUMENT_CUSTOMIZATION_TITLE,
            description=language.ARGUMENT_CUSTOMIZATION_DESCRIPTION,
        )
        # All applications use these: usefull, everone.

        information = self.parser.add_argument_group(
            title=language.ARGUMENT_INFORMATION_TITLE,
            description=language.ARGUMENT_INFORMATION_DESCRIPTION,
        )
        # Displays information then exits: useless, noone.

        modification = self.parser.add_argument_group(
            title=language.ARGUMENT_MODIFICATION_TITLE,
            description=language.ARGUMENT_MODIFICATION_DESCRIPTION,
        )
        # All applications use these: useless, everyone.

        arguments: APD = {}
        arguments[Application] = application
        arguments[Customization] = customization

        arguments[InformationConfiguration] = modification
        arguments[InformationHelp] = information
        arguments[InformationVersion] = information

        arguments[Positional] = application
        arguments[Optional] = application

        return arguments

    def _add_argument(self, sessions: list[SessionParse]) -> N:
        """"""
        arguments = self._make_argument_group()

        for session in sessions:
            for name, argument in session.items(self.core):
                if not argument.argument:
                    continue
                parser = arguments[argument]
                args = argument.key(name)
                star = argument.dictionary()
                parser.add_argument(*args, **star)

    def _add_attribute(self, sessions: list[SessionParse]) -> N:
        """"""
        section = self.core.application.name
        for session in sessions:
            for option, argument in session.items(self.core):
                if not argument.attribute:
                    continue

                override = getattr(self.args, option, NONE)
                database = self.configuration.get(section, option)
                fallback = argument.fallback

                value = override or database or fallback
                setattr(session, option, value)

                if override:
                    # Prepare for saving override values.
                    self.configuration.set(section, option, override)

    ######

    def _parse_args(self, known: B) -> N:
        """"""
        parser = self.parser
        argument_list = self.argument_list

        if known:
            self.args = parser.parse_known_args(argument_list)[0]
        else:
            self.args = parser.parse_args(argument_list)

    def __enter__(self):
        self.configuration.load()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        save = bool(getattr(self.args, CONFIGURATION, NONE))
        if save and override:
            self.configuration.save()
        return False

    def __init__(self, argument_list: L[S], exit_on_error: B) -> N:
        self.args = ""
        self.parser = None

        self.argument_list = argument_list
        self.configuration = Configuration()
        self.exit_on_error = exit_on_error

        self.core = Core(
            default.application(),
            default.interface(),
            default.language(),
        )
