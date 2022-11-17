"""Application for translating text to other languages."""
import argparse
import configparser

from celestine.keywords.all import LANGUAGE
from .keyword import NONE

from .keyword import KEY
from .keyword import REGION
from .keyword import URL

from .keyword import CONFIGURE
from .keyword import REPORT
from .keyword import TRANSLATE

from .keyword import STORE


def argument(arguments):
    """Build up the argument."""
    arguments.parser.add_argument(
        arguments.flag(KEY),
        arguments.name(KEY),
        action=STORE,
        help="A brief description of what the argument does.",
    )

    arguments.parser.add_argument(
        arguments.flag(REGION),
        arguments.name(REGION),
        action=STORE,
        help="A brief description of what the argument does.",
    )

    arguments.parser.add_argument(
        arguments.flag(URL),
        arguments.name(URL),
        action=STORE,
        help="A brief description of what the argument does.",
    )

    return argument


def attribute():
    """Build up the attribute file."""
    return [KEY, REGION, URL]


def default():
    """Build up the default file."""
    return [NONE, NONE, NONE]


def image_format():
    return []
