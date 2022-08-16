"""Application for translating text to other languages."""
import argparse
import configparser

from .keyword import LANGUAGE
from .keyword import NONE

from .keyword import KEY
from .keyword import REGION
from .keyword import URL

from .keyword import CONFIGURE
from .keyword import REPORT
from .keyword import TRANSLATE

from .keyword import STORE


def argument(argument):
    """Build up the argument."""
    configure = argument.subparser.add_parser(
        CONFIGURE,
        help="you are a fish",
    )

    configure.add_argument(
        KEY,
        action=STORE,
        help="A brief description of what the argument does.",
    )

    configure.add_argument(
        REGION,
        action=STORE,
        help="A brief description of what the argument does.",
    )

    configure.add_argument(
        URL,
        action=STORE,
        help="A brief description of what the argument does.",
    )

    report = argument.subparser.add_parser(
        REPORT,
        help="you are a fish",
    )

    translate = argument.subparser.add_parser(
        TRANSLATE,
        help="you are a fish",
    )

    return argument


def attribute():
    """Build up the attribute file."""
    return (KEY, REGION, URL)


def default():
    """Build up the default file."""
    return (NONE, NONE, NONE)
