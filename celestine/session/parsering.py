""""""


import argparse
from argparse import ArgumentParser as AP
from typing import TypeAlias as TA

from celestine import load
from celestine.parser.main import get_parser
from celestine.parser.parser import make_parser
from celestine.session.argument import (
    Application,
    Customization,
    InformationConfiguration,
    InformationHelp,
    InformationVersion,
    Optional,
    Positional,
)
from celestine.text.directory import (
    APPLICATION,
    INTERFACE,
    LANGUAGE,
)
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
from .session import (
    Dictionary,
    Session,
)
from .text import CONFIGURATION

INIT = "__init__"


# ADI: typing.TypeAlias = typing.Iterable[typing.Tuple[str, Argument]]

# APD: TA = D[U[Argument, T[Argument]], U[AP, AG]]
APD: TA = D[A, A]


def make_argument_group(language: MT, parser: AP) -> APD:
    """"""

    application = parser.add_argument_group(
        title=language.ARGUMENT_APPLICATION_TITLE,
        description=language.ARGUMENT_APPLICATION_DESCRIPTION,
    )
    """Your program stuff goes here: usefull, noone."""

    customization = parser.add_argument_group(
        title=language.ARGUMENT_CUSTOMIZATION_TITLE,
        description=language.ARGUMENT_CUSTOMIZATION_DESCRIPTION,
    )
    """All applications use these: usefull, everone."""

    information = parser.add_argument_group(
        title=language.ARGUMENT_INFORMATION_TITLE,
        description=language.ARGUMENT_INFORMATION_DESCRIPTION,
    )
    """Displays information then exits: useless, noone."""

    modification = parser.add_argument_group(
        title=language.ARGUMENT_MODIFICATION_TITLE,
        description=language.ARGUMENT_MODIFICATION_DESCRIPTION,
    )
    """All applications use these: useless, everyone."""

    arguments: APD = {}
    arguments[Application] = application
    arguments[Customization] = customization

    arguments[InformationConfiguration] = modification
    arguments[InformationHelp] = information
    arguments[InformationVersion] = information

    arguments[Positional] = application
    arguments[Optional] = application

    return arguments


def add_argument(sessions: list[Session], arguments: APD) -> N:
    """"""
    for session in sessions:
        for name, argument in session.items():
            if not argument.argument:
                continue
            parser = arguments[argument]
            args = argument.key(name)
            star = argument.dictionary()
            parser.add_argument(*args, **star)


def add_attribute(
    sessions: list[Session],
    configuration: Configuration,
    args: argparse.Namespace,
) -> N:
    """"""
    save = bool(getattr(args, CONFIGURATION, NONE))
    for session in sessions:
        for option, argument in session.items():
            if not argument.attribute:
                continue

            section = load.module_to_name(session.application)

            override = getattr(args, option, NONE)
            database = configuration.get(section, option)
            fallback = argument.fallback
            default = getattr(session, option, None)
            # default is a module and that is cheating

            value = override or database or fallback or default
            setattr(session, option, value)
            if save and override:
                configuration.set(section, option, override)


def get_parser_batch(
    argv: L[S],
    exit_on_error: B,
    application: MT,
    language: MT,
    attributes: L[Session],
    fast: B,
    configuration: Configuration,
) -> L[Dictionary]:
    """"""
    parser = make_parser(language, exit_on_error)

    arguments = make_argument_group(language, parser)

    add_argument(attributes, arguments)

    parse_known_args = parser.parse_known_args
    parse_args = parser.parse_args
    args = parse_known_args(argv)[0] if fast else parse_args(argv)

    add_attribute(attributes, configuration, args)

    return attributes


def get_parser(
    argv: L[S],
    exit_on_error: B,
    application: MT,
    language: MT,
    attribute: Session,
    fast: B,
    configuration: Configuration,
) -> L[Dictionary]:
    """"""

    return get_parser_batch(
        argv,
        exit_on_error,
        application,
        language,
        [attribute],
        fast,
        configuration,
    )[0]


from celestine.parser.default import quick

SESSION = "session"


class Holder:
    application: MT
    attribute: L[S]
    interface: MT
    language: MT
    call: MT
    view: MT

    def __init__(self):
        self.attribute = None
        self.interface = None
        self.language = None
        self.call = None
        self.view = None


def start_session(argv: L[S], exit_on_error: B = True) -> Session:
    """"""

    def parse(holder, name, default) -> MT:
        """Quickly parse important attributes."""

        class_name = name.capitalize()
        session = load.method(class_name, SESSION, SESSION)

        hippo = session.clone(holder)

        parser = get_parser(
            argv,
            exit_on_error,
            holder.application,
            holder.language,
            hippo,
            True,
            configuration,
        )

        return parser

    configuration = Configuration()
    configuration.load()

    state = quick()
    state = parse(state, LANGUAGE, state.language)
    state = parse(state, INTERFACE, state.interface)
    state = parse(state, APPLICATION, state.application)

    session1 = load.method("Session", "session", "session")
    session2 = getattr(state.application, "Session")
    session3 = load.method("Information", "session", "session")

    hippos = [
        session1.clone(state),
        session3.clone(state),
        session2.clone(state),
    ]
    attribute = get_parser_batch(
        argv,
        exit_on_error,
        state.application,
        state.language,
        hippos,
        True,
        configuration,
    )

    session = attribute[0]
    session.attribute = attribute[1]

    configuration.save()

    new_session = Holder()

    the_name = load.module_to_name(session.application)

    call = load.functions(load.module(APPLICATION, the_name, "call"))
    view = load.functions(load.module(APPLICATION, the_name, "view"))

    new_session.application = session.application
    new_session.attribute: attribute[1]
    new_session.interface = session.interface
    new_session.language = session.language
    new_session.call = call
    new_session.view = view
    new_session.main = "main"
    return new_session

    # override for demo
    # return session


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


"""Configuration information will show your saved stuff."""
