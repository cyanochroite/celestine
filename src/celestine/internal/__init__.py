"""Load and save user settings from a file."""
import configparser


from celestine.keyword.all import CELESTINE


from .keyword import APPLICATION
from .keyword import LANGUAGE
from .keyword import PYTHON

from celestine.keyword.all import application
from celestine.keyword.all import language
from celestine.keyword.all import python


TERMINAL = "terminal"
ENGLISH = "english"
PYTHON_3_10 = "python_3_10"
CELESTINE = "celestine"
CONFIGURE = "configure"
STORE = "store"


def argument(argument):
    """Build up the argument."""
    configure = argument.subparser.add_parser(
        CONFIGURE,
        help="you are a fish",
    )

    configure.add_argument(
        "_" + APPLICATION,
        action=STORE,
        choices=application,
        help="A brief description of what the argument does.",
    )

    configure.add_argument(
        LANGUAGE,
        action=STORE,
        choices=language,
        help="A brief description of what the argument does.",
    )

    configure.add_argument(
        PYTHON,
        action=STORE,
        choices=python,
        help="A brief description of what the argument does.",
    )

    return argument


def default():
    """Build up the default file."""
    return (TERMINAL, ENGLISH, PYTHON_3_10, "main")


def attribute():
    """Build up the attribute file."""
    return (APPLICATION, LANGUAGE, PYTHON, "task")


def image_format():
    return []
