""""""


import argparse
from typing import TypeAlias as TA

from celestine import load
from celestine.parser.parser import make_parser
from celestine.session.configuration import Configuration
from celestine.session.session import Session as SessionParse
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

# ADI: typing.TypeAlias = typing.Iterable[typing.Tuple[str, Argument]]

# APD: TA = D[U[Argument, T[Argument]], U[AP, AG]]
APD: TA = D[A, A]


def add_argument(sessions: list[SessionParse], arguments: APD) -> N:
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
    sessions: list[SessionParse],
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
    fast: B,
):
    """Attributes is modified in place."""

    parse_known_args = parser.parse_known_args
    parse_args = parser.parse_args
    parse_known_args(argv)[0] if fast else parse_args(argv)


def get_parser(
    argv: L[S],
    exit_on_error: B,
    application: MT,
    language: MT,
    attributes: L[SessionParse],
    fast: B,
    configuration: Configuration,
):
    """Attributes is modified in place."""
    parser = make_parser(language, exit_on_error)

    arguments = make_argument_group(language, parser)

    add_argument(attributes, arguments)

    parse_known_args = parser.parse_known_args
    parse_args = parser.parse_args
    args = parse_known_args(argv)[0] if fast else parse_args(argv)

    add_attribute(attributes, configuration, args)
