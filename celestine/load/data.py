""""""

from celestine.file.string import string
from celestine.unicode import (
    FULL_STOP,
    LATIN_SMALL_LETTER_C,
    LATIN_SMALL_LETTER_F,
    LATIN_SMALL_LETTER_I,
    LATIN_SMALL_LETTER_N,
    LATIN_SMALL_LETTER_O,
    LATIN_SMALL_LETTER_P,
    LATIN_SMALL_LETTER_T,
    LATIN_SMALL_LETTER_U,
    LATIN_SMALL_LETTER_Y,
    LESS_THAN_SIGN,
    SPACE,
)

FUNCTION = string(
    LESS_THAN_SIGN,
    LATIN_SMALL_LETTER_F,
    LATIN_SMALL_LETTER_U,
    LATIN_SMALL_LETTER_N,
    LATIN_SMALL_LETTER_C,
    LATIN_SMALL_LETTER_T,
    LATIN_SMALL_LETTER_I,
    LATIN_SMALL_LETTER_O,
    LATIN_SMALL_LETTER_N,
    SPACE,
)

PYTHON_EXTENSION = string(
    FULL_STOP,
    LATIN_SMALL_LETTER_P,
    LATIN_SMALL_LETTER_Y,
)


def clamp(minimum, midterm, maximum):
    """The order of the inputs actually don't matter."""
    return sorted((minimum, midterm, maximum))[1]
