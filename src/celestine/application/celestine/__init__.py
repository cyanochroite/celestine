"""Load and save user settings from a file."""
import configparser


from celestine.keyword.main import CELESTINE


from celestine.application.terminal.keyword import APPLICATION
from celestine.application.terminal.keyword import LANGUAGE
from celestine.application.terminal.keyword import PYTHON

from celestine.keyword.main import application
from celestine.keyword.main import language
from celestine.keyword.main import python


TERMINAL = "terminal"
ENGLISH = "english"
PYTHON_3_10 = "python_3_10"
CELESTINE = "celestine"
CONFIGURE = "configure"
STORE = "store"


def argument(argument):
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


def default(configuration):
    configuration.set(CELESTINE, APPLICATION, TERMINAL)
    configuration.set(CELESTINE, LANGUAGE, ENGLISH)
    configuration.set(CELESTINE, PYTHON, PYTHON_3_10)
    return configuration


def attribute(attribute):
    """Build up the attribute file."""
    return attribute.add(CELESTINE, APPLICATION, LANGUAGE, PYTHON, "task")
