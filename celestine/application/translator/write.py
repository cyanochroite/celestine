"""Takes care of writting files to disk."""

import io
import keyword

from celestine.data import normalize
from celestine.stream import Module
from celestine.typed import (
    GS,
    TABLE,
    N,
    S,
)
from celestine.unicode import (
    EQUALS_SIGN,
    FULL_STOP,
    INFORMATION_SEPARATOR_FOUR,
    LINE_FEED,
    LINE_SEPARATOR,
    PARAGRAPH_SEPARATOR,
    QUOTATION_MARK,
    SPACE,
)

from .data import (
    INIT,
    LANGUAGE,
    LANGUAGE_NAME_ENGLISH,
    LANGUAGE_NAME_NATIVE,
    LANGUAGE_TAG_ISO,
)


def dictionary_to_string(dictionary: TABLE) -> GS:
    """Prepares the dictionary to be written to a file."""
    dictionary_items = dictionary.items()
    sorted_items = sorted(dictionary_items)
    for identifier, expression in sorted_items:
        if not identifier.isidentifier():
            raise ValueError("Not a valid identifier.")
        if keyword.iskeyword(identifier):
            raise ValueError("This word is a keyword.")
        if keyword.issoftkeyword(identifier):
            raise ValueError("This word is a soft keyword.")

        yield from LINE_FEED
        yield from LINE_SEPARATOR

        yield from identifier
        yield from SPACE
        yield from EQUALS_SIGN
        yield from SPACE
        yield from QUOTATION_MARK
        yield from INFORMATION_SEPARATOR_FOUR

        character = normalize.characters(expression)
        whitespace = normalize.whitespace(character)
        quotation = normalize.quotation(whitespace)
        punctuation = normalize.punctuation(quotation)
        yield from punctuation

        yield from QUOTATION_MARK
        yield from LINE_FEED
        yield from LINE_SEPARATOR


def language_file(translation: TABLE, overridden: TABLE) -> GS:
    """Print translations first then print overridden values."""
    lookup = translation | overridden
    yield from QUOTATION_MARK
    yield from QUOTATION_MARK
    yield from QUOTATION_MARK
    yield from lookup[LANGUAGE_NAME_ENGLISH]
    yield from SPACE
    yield from lookup[LANGUAGE_NAME_NATIVE]
    yield from SPACE
    yield from lookup[LANGUAGE_TAG_ISO]
    yield from FULL_STOP
    yield from QUOTATION_MARK
    yield from QUOTATION_MARK
    yield from QUOTATION_MARK
    yield from LINE_FEED
    yield from LINE_SEPARATOR
    yield from dictionary_to_string(translation)
    yield from PARAGRAPH_SEPARATOR
    yield from dictionary_to_string(overridden)


def make_init_file():
    """Create the package __init__ file."""
    string = io.StringIO()
    string.write(QUOTATION_MARK)
    string.write(QUOTATION_MARK)
    string.write(QUOTATION_MARK)
    string.write(QUOTATION_MARK)
    string.write(QUOTATION_MARK)
    string.write(QUOTATION_MARK)
    string.write(LINE_FEED)
    string.write(LINE_SEPARATOR)

    value = string.getvalue()
    width = normalize.wrap(value)
    Module.save(width, LANGUAGE, INIT)


def save_language(translation: TABLE, overridden: TABLE, *path: S) -> N:
    """Save a language file to disk."""
    file = language_file(translation, overridden)
    string = normalize.wrap(file)
    Module.save(string, *path)
