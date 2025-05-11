""""""

import argparse
import sys

from celestine import (
    bank,
    load,
)
from celestine.literal import (
    CELESTINE,
    NONE,
)
from celestine.session.argument import (
    Application,
    Customization,
    InformationConfiguration,
    InformationHelp,
    InformationVersion,
    Optional,
    Positional,
)
from celestine.session.data import Values
from celestine.typed import (
    DA,
    A,
    B,
    D,
    L,
    N,
    S,
    ignore,
)

SESSION = "session"


class SessionParse:
    """Typing info only.

    Reflecting Session from Session
    """

    main: S

    @classmethod
    def dictionary(cls) -> DA:
        """"""
        ignore(cls)
        return {}


ERROR = "error"
INIT = "__init__"
TRANSLATE_THIS = "unrecognized arguments"

# ADI: typing.TypeAlias = typing.Iterable[typing.Tuple[str, Argument]]
# APD: TA = D[U[Argument, T[Argument]], U[AP, AG]]
type APD = D[A, A]


class Magic:
    """"""

    args: argparse.Namespace
    parser: argparse.ArgumentParser

    def get_parser(self, attributes: L[SessionParse], known: B) -> N:
        """
        All parser magic happens here.

        A lot of behind the scenes stuff going on here.

        Creates a new parser object.
        Populates it with arguments to parse.
        Parses the arguments with provided attributes.
        Adds the parsed objects to class objects
        """
        self.parser = argparse.ArgumentParser(
            prog=CELESTINE,
            add_help=False,
        )

        self._add_argument(attributes)

        self._parse_args(known)

        self._add_attribute(attributes)

    def parse(self, name: S) -> N:
        """Quickly parse important attributes."""
        method = load.method(name.capitalize(), SESSION, SESSION)
        self.get_parser([method], True)
        value = getattr(method, name)
        module = load.module(name, value)
        setattr(bank, name, module)

    ###

    def _make_argument_group(self) -> APD:
        """"""

        language = bank.language

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
            for name, argument in session.items():
                if not argument.arguments:
                    continue
                parser = arguments[argument]
                args = argument.key(name)
                star = argument.dictionary()
                parser.add_argument(*args, **star)

    def _add_attribute(self, sessions: list[SessionParse]) -> N:
        """"""
        section = bank.application.__spec__.name
        for session in sessions:
            for option, argument in session.items():
                if not argument.attribute:
                    continue

                override = getattr(self.args, option, NONE)
                database = bank.configuration.get(section, option)
                fallback = argument.fallback

                value = override or database or fallback
                setattr(session, option, value)

                if override:
                    # Prepare for saving override values.
                    bank.configuration.set(section, option, override)

    ######

    def _parse_args(self, known: B) -> N:
        """"""
        parser = self.parser
        argument_list = sys.argv[1:]

        if known:
            self.args = parser.parse_known_args(argument_list)[0]
        else:
            self.args = parser.parse_args(argument_list)

    def __enter__(self):
        bank.configuration.load()
        return self

    def __exit__(self, *_):
        save = bool(getattr(self.args, Values.CONFIGURATION, NONE))
        if save:
            bank.configuration.save()
        return False

    def __init__(self) -> N:
        self.args = argparse.Namespace()
        self.parser = argparse.ArgumentParser()
