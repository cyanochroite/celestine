"""Application for translating text to other languages."""
import typing

from celestine.session.argument import Argument

from celestine.text.unicode import NONE

from .text import KEY
from .text import REGION
from .text import URL

from .text import STORE


def add_argument(argument: Argument) -> None:
    """Build up the argument."""
    argument.parser.add_argument(
        argument.flag(KEY),
        argument.name(KEY),
        action=STORE,
        help="A brief description of what the argument does.",
    )

    argument.parser.add_argument(
        argument.flag(REGION),
        argument.name(REGION),
        action=STORE,
        help="A brief description of what the argument does.",
    )

    argument.parser.add_argument(
        argument.flag(URL),
        argument.name(URL),
        action=STORE,
        help="A brief description of what the argument does.",
    )


def attribute() -> typing.Dict[str, str]:
    return {
        KEY: NONE,
        REGION: NONE,
        URL: NONE,
    }

