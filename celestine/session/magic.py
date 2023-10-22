""""""

import argparse
import dataclasses

from celestine import load
from celestine.session.argument import (
    Application,
    Customization,
    InformationConfiguration,
    InformationHelp,
    InformationVersion,
    Optional,
    Positional,
)
from celestine.session.data import CONFIGURATION
from celestine.typed import (
    LS,
    A,
    B,
    D,
    L,
    M,
    N,
)
from celestine.unicode import NONE

from . import default
from .configuration import Configuration
from .data import SESSION
from .parser import parser as make_parser
from .session import Session as SessionParse

ERROR = "error"
INIT = "__init__"
TRANSLATE_THIS = "unrecognized arguments"

# ADI: typing.TypeAlias = typing.Iterable[typing.Tuple[str, Argument]]
# APD: TA = D[U[Argument, T[Argument]], U[AP, AG]]
type APD = D[A, A]


class Magic:
    """"""

    @dataclasses.dataclass
    class Core:
        """"""

        application: M
        interface: M
        language: M

        def __setattr__(self, name, value):
            module = load.module(name, value)
            module.name = value
            super().__setattr__(name, module)

    core: Core
    args: argparse.Namespace
    parser: argparse.ArgumentParser

    argument_list: LS
    configuration: Configuration
    exit_on_error: B

    def get_parser(self, attributes: L[SessionParse], known: B) -> N:
        """
        All parser magic happens here.

        A lot of behind the scenes stuff going on here.

        Creates a new parser object.
        Populates it with arguments to parse.
        Parses the arguments with provided attributes.
        Adds the parsed objects to class objects
        """

        self._make_parser()

        self._add_argument(attributes)

        self._parse_args(known)

        self._add_attribute(attributes)

    def parse(self, name) -> N:
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
            # TODO: Make class instance for less weird classmethods
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

    def _make_parser(self):
        """"""
        language = self.core.language
        exit_on_error = self.exit_on_error
        self.parser = make_parser(language, exit_on_error)

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

    def __exit__(self, *_):
        save = bool(getattr(self.args, CONFIGURATION, NONE))
        if save:
            self.configuration.save()
        return False

    def __init__(self, argument_list: LS, exit_on_error: B) -> N:
        self.args = argparse.Namespace()
        self.parser = argparse.ArgumentParser()

        self.argument_list = argument_list
        self.configuration = Configuration()
        self.exit_on_error = exit_on_error

        self.core = self.Core(
            default.application(),
            default.interface(),
            default.language(),
        )
