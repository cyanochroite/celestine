"""The Code page."""

from celestine import load
from celestine.data import call
from celestine.typed import (
    B,
    R,
)

from .main import do_translate


@call
def translate() -> B:
    """Translate the language files."""
    do_translate()


@call
def train(**star: R) -> B:
    """The main function."""
    minimum = {}
    maximum = {}
    language = load.argument(LANGUAGE)
    for lang in language:
        dictionary = load.dictionary(LANGUAGE, lang)
        for key, value in dictionary.items():
            length = len(value)
            minimum[key] = min(length, minimum.get(key, 256))
            maximum[key] = max(length, maximum.get(key, 0))

    return {"min": minimum, "max": maximum}
