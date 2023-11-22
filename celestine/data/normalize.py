"""Central place for loading and importing external files."""

import io

from celestine.stream.data import (
    MAXIMUM_LINE_LENGTH,
    SECTION_BREAK,
)
from celestine.typed import (
    GS,
    S,
)
from celestine.unicode import (
    APOSTROPHE,
    INFORMATION_SEPARATOR_FOUR,
    INFORMATION_SEPARATOR_ONE,
    INFORMATION_SEPARATOR_THREE,
    INFORMATION_SEPARATOR_TWO,
    LINE_FEED,
    LINE_SEPARATOR,
    PARAGRAPH_SEPARATOR,
    QUOTATION_MARK,
    REVERSE_SOLIDUS,
    SPACE,
)
from celestine.unicode.alphabet2 import (
    DIRECTIONAL_FORMATTING,
    UNICODE,
    unicode_break_hard,
    unicode_break_soft,
    unicode_identifier,
    unicode_newline,
    unicode_punctuation,
    unicode_whitespace,
)


def wrap(string: S) -> GS:
    """
    Wrap long lines by breaking on punctiation or spaces.

    PARAGRAPH_SEPARATOR indicates a seperator should be printed.
    LINE_SEPARATOR indicates end of line. Reset column.

    The following breaks on long lines.
    Higher number has higher priority.
    INFORMATION_SEPARATOR_FOUR indicates begining of string.
    INFORMATION_SEPARATOR_THREE indicates hard punctuation.
    INFORMATION_SEPARATOR_TWO indicates soft punctuation.
    INFORMATION_SEPARATOR_ONE indicates whitespace.

    A long line will always break on a punctuation if one can be found.
    If not the line will break on a whitespace if one can be found.
    Otherwise hard break on the last character and hope for the best.
    """
    buffer = io.StringIO()
    size = 0

    count = 0
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0

    for character in string:
        if character == PARAGRAPH_SEPARATOR:
            yield from LINE_FEED
            yield from SECTION_BREAK
            yield from LINE_FEED
            continue

        if character == LINE_SEPARATOR:
            buffer.seek(0, io.SEEK_SET)
            line = buffer.read(count)
            buffer.seek(0, io.SEEK_SET)

            count = 0
            count_a = 0
            count_b = 0
            count_c = 0
            count_d = 0

            yield from line
            continue

        if character == INFORMATION_SEPARATOR_FOUR:
            count_d = count
            continue

        if character == INFORMATION_SEPARATOR_THREE:
            count_c = count
            continue

        if character == INFORMATION_SEPARATOR_TWO:
            count_b = count
            continue

        if character == INFORMATION_SEPARATOR_ONE:
            count_a = count
            continue

        size = len(character)
        if count + size >= MAXIMUM_LINE_LENGTH:
            buffer.seek(0, io.SEEK_SET)

            pull = 0
            if 0 < count_d < MAXIMUM_LINE_LENGTH:
                pull = count_d
            elif 0 < count_c < MAXIMUM_LINE_LENGTH:
                pull = count_c
            elif 0 < count_b < MAXIMUM_LINE_LENGTH:
                pull = count_b
            elif 0 < count_a < MAXIMUM_LINE_LENGTH:
                pull = count_a
            else:
                pull = MAXIMUM_LINE_LENGTH

            data = buffer.read(pull)

            yield from data
            yield from REVERSE_SOLIDUS
            yield from LINE_FEED

            string = buffer.read(count - pull)

            buffer.seek(0, io.SEEK_SET)

            count = buffer.write(string)
            count_a = max(0, count_a - pull)
            count_b = max(0, count_b - pull)
            count_c = max(0, count_c - pull)
            count_d = max(0, count_d - pull)

        count += buffer.write(character)

        if character == LINE_FEED:
            buffer.seek(0, io.SEEK_SET)
            # yield from buffer.read(count)

            candy = buffer.read(count)
            yield from candy
            buffer.seek(0, io.SEEK_SET)

            count = 0
            count_a = 0
            count_b = 0
            count_c = 0
            count_d = 0

    buffer.seek(0, io.SEEK_SET)
    yield from buffer.read(count)


def wrap_text(string: S) -> GS:
    """"""
    buffer = io.StringIO()

    count = 0
    count_a = 0

    for character in string:
        count += buffer.write(character)

        if character == LINE_FEED:
            buffer.seek(0, io.SEEK_SET)
            line = buffer.read(count)
            buffer.seek(0, io.SEEK_SET)

            count = 0
            count_a = 0

            yield from line
            continue

        if count > MAXIMUM_LINE_LENGTH:
            buffer.seek(0, io.SEEK_SET)

            pull = 0
            if 0 < count_a < MAXIMUM_LINE_LENGTH:
                pull = count_a
            else:
                pull = MAXIMUM_LINE_LENGTH

            data = buffer.read(pull)

            yield from data
            yield from LINE_FEED

            string = buffer.read(count - pull)

            buffer.seek(0, io.SEEK_SET)

            count = buffer.write(string)
            count_a = max(0, count_a - pull)

        if character == SPACE:
            count_a = count

    buffer.seek(0, io.SEEK_SET)
    yield from buffer.read(count)


def character(string: S) -> GS:
    """Remove all invalid characters."""
    for character in string:
        if character not in UNICODE:
            continue

        if character in DIRECTIONAL_FORMATTING:
            continue

        yield from character


def newline(string: S) -> GS:
    """Remove all newline characters."""
    for character in string:
        if character in unicode_newline:
            yield from SPACE
        else:
            yield from character


def whitespace(string: S) -> GS:
    """
    Remove (ignore) all whitespace from the front and end of the string.

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


def quotation(string: S) -> GS:
    """"""
    for character in string:
        if character == QUOTATION_MARK:
            yield from APOSTROPHE
        else:
            yield from character


def punctuation(string: S) -> GS:
    """Remove duplicate punctiation symbols."""

    previous = None
    for character in string:
        if character in unicode_punctuation:
            if character == previous:
                continue
        yield character
        previous = character
