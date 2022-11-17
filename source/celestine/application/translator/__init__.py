"""Application for translating text to other languages."""

from celestine.string.all import LANGUAGE

from celestine.application.translator.keyword import NONE

from celestine.application.translator.keyword import KEY
from celestine.application.translator.keyword import REGION
from celestine.application.translator.keyword import URL

from celestine.application.translator.keyword import CONFIGURE
from celestine.application.translator.keyword import REPORT
from celestine.application.translator.keyword import TRANSLATE

from celestine.application.translator.keyword import STORE


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
