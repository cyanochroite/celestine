""""""

import os

from celestine.session.argument import Argument

from .text import DIRECTORY


def add_argument(
    argument: Argument
) -> None:
    """"""

    argument.add_argument(
        default=os.getcwd(),
        description="",
        name=DIRECTORY,
        required=False,
    )

