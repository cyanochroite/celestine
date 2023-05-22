"""Central place for loading and importing external files."""

from celestine.alphabet import (
    DIRECTIONAL_FORMATTING,
    UNICODE,
    unicode_break_hard,
    unicode_break_soft,
    unicode_identifier,
    unicode_punctuation,
    unicode_whitespace,
)
from celestine.unicode import (
    APOSTROPHE,
    INFORMATION_SEPARATOR_ONE,
    INFORMATION_SEPARATOR_THREE,
    INFORMATION_SEPARATOR_TWO,
    QUOTATION_MARK,
    SPACE,
)


def character(string):
    """Remove all invalid characters."""
    for character in string:
        if character not in UNICODE:
            continue

        if character in DIRECTIONAL_FORMATTING:
            continue

        yield from character


def whitespace(string):
    """
    Remove (ignore) all whitespace from the start and end of the string.

    Convert all whitespace to spaces.
    Remove all duplicate spaces.
    Preserve space between words.
    Remove space before punctuation.
    Ensure space after every punctuation.
    Allow line breaks after punctuation.
    """
    previous = None
    whitespace = None

    for character in string:
        if character in unicode_identifier:
            if previous in unicode_break_soft:
                yield from SPACE
                yield from INFORMATION_SEPARATOR_TWO
            elif previous in unicode_break_hard:
                yield from SPACE
                yield from INFORMATION_SEPARATOR_THREE
            elif previous in unicode_identifier:
                # Preserve space between words.
                if whitespace:
                    yield from SPACE
                    yield from INFORMATION_SEPARATOR_ONE

        whitespace = character in unicode_whitespace

        if not whitespace:
            yield from character
            previous = character


def quotation(string):
    """"""

    for character in string:
        if character == QUOTATION_MARK:
            yield from APOSTROPHE
        else:
            yield from character


def punctuation(string):
    """Remove duplicate punctiation symbols."""

    previous = None
    for character in string:
        if character in unicode_punctuation:
            if character == previous:
                continue
        yield character
        previous = character


def normalize(string):
    """"""
    _character = character(string)
    _whitespace = whitespace(_character)
    _quotation = quotation(_whitespace)
    _punctuation = punctuation(_quotation)
    yield from _punctuation
