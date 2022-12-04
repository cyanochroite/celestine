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

    argument.add_optional(
        KEY,
        "",
        NONE,
    )

    argument.add_optional(
        REGION,
        "",
        NONE,
    )

    argument.add_optional(
        URL,
        "",
        NONE,
    )
