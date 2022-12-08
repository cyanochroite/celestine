""""""

import os
import dataclasses

from celestine.session.argument import Argument
from celestine.session.argument import Optional

from .main import window
from .text import DIRECTORY


def add_argument(
    argument: Argument
) -> None:
    """"""

    argument.add_optional(
        DIRECTORY,
        "",
        os.getcwd(),
    )


@dataclasses.dataclass
class Attribute():
    """"""

    directory = Optional(os.getcwd())


def main(_):
    return [
        window,
    ]
