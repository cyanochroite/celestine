""""""


import argparse
from typing import TypeAlias as TA

from celestine import load
from celestine.parser.parser import make_parser
from celestine.session.configuration import Configuration
from celestine.session.session import (
    Dictionary,
    Session,
)
from celestine.session.text import CONFIGURATION
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

from .argument import make_argument_group
from .parser import make_parser

# APD: TA = D[U[Argument, T[Argument]], U[AP, AG]]
APD: TA = D[A, A]


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
            override = getattr(args, option, NONE)
            section = load.module_to_name(session._application)

            database = configuration.get(section, option)
            value = override or database or argument.fallback
            setattr(session, option, value)
            if save and override:
                configuration.set(section, option, override)


def get_parser(
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
