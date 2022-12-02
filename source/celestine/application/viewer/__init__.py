import os

from celestine.session.argument import Argument

from .text import DIRECTORY


def add_argument(argument: Argument) -> None:
    argument.parser.add_argument(
        argument.flag(DIRECTORY),
        argument.name(DIRECTORY),
    )


def attribute() -> None:
    return {
        DIRECTORY: os.getcwd(),
    }


def default():
    """Build up the default file."""
    return ["main"]


def attribute():
    """Build up the attribute file."""
    return ["task"]

