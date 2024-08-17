"""The Code page."""

from celestine import load
from celestine.data import call
from celestine.typed import (
    B,
    D,
    R,
    S,
)

from .main import do_translate


@call
def translate(**star: R) -> B:
    """Translate the language files."""
    do_translate()
    return True


@call
def train(**star: R) -> B:
    """The main function."""
    minimum: D[S, S] = {}
    maximum: D[S, S] = {}
    language = load.argument("language")
    for lang in language:
        dictionary = load.dictionary("language", lang)
        for key, value in dictionary.items():
            length = len(value)
            minimum[key] = min(length, minimum.get(key, 256))
            maximum[key] = max(length, maximum.get(key, 0))
    print({"min": minimum, "max": maximum})
    return True
