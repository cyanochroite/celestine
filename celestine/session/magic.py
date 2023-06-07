""""""


from typing import TypeAlias as TA

from celestine import load
from celestine.parser import default
from celestine.parser.argument import make_argument_group
from celestine.parser.parser import make_parser
from celestine.session.configuration import Configuration
from celestine.session.data import CONFIGURATION
from celestine.session.session import Session as SessionParse
from celestine.typed import (
    MT,
    A,
    B,
    D,
    L,
    N,
    S,
)
from celestine.unicode import NONE

from .configuration import Configuration
from .data import SESSION
from .session import Session as SessionParse

# ADI: typing.TypeAlias = typing.Iterable[typing.Tuple[str, Argument]]

# APD: TA = D[U[Argument, T[Argument]], U[AP, AG]]
APD: TA = D[A, A]


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


class Magic:
    def add_argument(
        self, sessions: list[SessionParse], arguments
    ) -> N:
        """"""

        for session in sessions:
            for name, argument in session.items(self.core):
                if not argument.argument:
                    continue
                parser = arguments[argument]
                args = argument.key(name)
                star = argument.dictionary()
                parser.add_argument(*args, **star)

    def add_attribute(self, sessions: list[SessionParse]) -> N:
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

    def get_parser(
        self,
        attributes: L[SessionParse],
        fast: B,
    ):
        """Attributes is modified in place."""

        parser = make_parser(self.core.language, self.exit_on_error)

        arguments = make_argument_group(self.core.language, parser)
        self.add_argument(attributes, arguments)

        if fast:
            self.args = parser.parse_known_args(self.argument_list)[0]
        else:
            self.args = parser.parse_args(self.argument_list)

        self.add_attribute(attributes)

    def parse(self, name) -> MT:
        """Quickly parse important attributes."""
        method = load.method(name.capitalize(), SESSION, SESSION)
        self.get_parser([method], True)
        setattr(self.core, name, getattr(method, name))

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

        self.argument_list = argument_list
        self.configuration = Configuration()
        self.exit_on_error = exit_on_error

        self.core = Core(
            default.application(),
            default.interface(),
            default.language(),
        )
