"""Application for translating text to other languages."""

from celestine.session.argument import Argument

from celestine.text.unicode import NONE

from .text import KEY
from .text import REGION
from .text import URL


def add_argument(
    argument: Argument
) -> None:
    """Build up the argument."""

    argument.add_argument(
        default=NONE,
        description="",
        name=KEY,
        required=False,
    )

    argument.add_argument(
        default=NONE,
        description="",
        name=REGION,
        required=False,
    )

    argument.add_argument(
        default=NONE,
        description="",
        name=URL,
        required=False,
    )
