""""""

from celestine import load

from .main import do_translate


def translate(*, session, **star):
    """Translate the language files."""

    do_translate(session)


def train():
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
