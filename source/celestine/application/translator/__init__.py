"""Application for translating text to other languages."""

from celestine.text.all import LANGUAGE

from .text import NONE

from .text import KEY
from .text import REGION
from .text import URL

from .text import CONFIGURE
from .text import REPORT
from .text import TRANSLATE

from .text import STORE


def argument(arguments):
    """Build up the argument."""
    arguments.parser.add_argument(
        arguments.flag(KEY),
        arguments.name(KEY),
        action=STORE,
        help="A brief description of what the argument does.",
    )

    arguments.parser.add_argument(
        arguments.flag(REGION),
        arguments.name(REGION),
        action=STORE,
        help="A brief description of what the argument does.",
    )

    arguments.parser.add_argument(
        arguments.flag(URL),
        arguments.name(URL),
        action=STORE,
        help="A brief description of what the argument does.",
    )

    return argument


def attribute():
    """Build up the attribute file."""
    return [KEY, REGION, URL]


def default():
    """Build up the default file."""
    return [NONE, NONE, NONE]


def image_format():
    return []
