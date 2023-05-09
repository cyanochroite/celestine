"""Central place for loading and importing external files."""

from celestine.unicode import (
    CARRIAGE_RETURN,
    CHARACTER_TABULATION,
    COLON,
    COMMA,
    EXCLAMATION_MARK,
    FORM_FEED,
    FULL_STOP,
    INFORMATION_SEPARATOR_FOUR,
    INFORMATION_SEPARATOR_ONE,
    INFORMATION_SEPARATOR_THREE,
    INFORMATION_SEPARATOR_TWO,
    LINE_FEED,
    LINE_SEPARATOR,
    LINE_TABULATION,
    NEXT_LINE,
    PARAGRAPH_SEPARATOR,
    QUESTION_MARK,
    SEMICOLON,
    SPACE,
)

MAXIMUM_LINE_LENGTH = 72

unicode_break_hard = frozenset(
    {
        COLON,
        EXCLAMATION_MARK,
        FULL_STOP,
        QUESTION_MARK,
    }
)

unicode_break_soft = frozenset(
    {
        COMMA,
        SEMICOLON,
    }
)

unicode_punctuation = unicode_break_hard | unicode_break_soft


unicode_whitespace = frozenset(
    {
        CARRIAGE_RETURN,
        CHARACTER_TABULATION,
        FORM_FEED,
        INFORMATION_SEPARATOR_FOUR,
        INFORMATION_SEPARATOR_THREE,
        INFORMATION_SEPARATOR_TWO,
        INFORMATION_SEPARATOR_ONE,
        LINE_FEED,
        LINE_SEPARATOR,
        LINE_TABULATION,
        NEXT_LINE,
        PARAGRAPH_SEPARATOR,
        SPACE,
    }
)

plane_0 = set({})

for index in range(0x10000):
    plane_0.add(chr(index))

basic_multilingual_plane = frozenset(plane_0)

not_identifier = unicode_punctuation | unicode_whitespace

unicode_identifier = basic_multilingual_plane - not_identifier


def normalize(string):
    """"""
    _character(string)
    _whitespace(_character)
    yield from punctuation


def _character(string):
    """Remove all invalid characters."""
    for character in string:
        if character in basic_multilingual_plane:
            yield from character


def _whitespace(string):
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
