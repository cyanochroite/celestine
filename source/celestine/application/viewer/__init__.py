import os

from celestine.session.argument import Argument

from .string import DIRECTORY


def add_argument(argument: Argument) -> None:
    argument.parser.add_argument(
        argument.flag(DIRECTORY),
        argument.name(DIRECTORY),
    )


def attribute() -> None:
    return {
        DIRECTORY: os.getcwd(),
    }
