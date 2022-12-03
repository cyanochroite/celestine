import os
import typing

from celestine.session.argument import Argument

from .text import DIRECTORY


def add_argument(argument: Argument) -> None:
    argument.parser.add_argument(
        argument.flag(DIRECTORY),
        argument.name(DIRECTORY),
    )


def attribute() -> typing.Dict[str, str]:
    return {
        DIRECTORY: os.getcwd(),
    }

