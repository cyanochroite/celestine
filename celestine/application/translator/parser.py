"""Central place for loading and importing external files."""
import io
import keyword

from celestine.unicode import (
    APOSTROPHE,
    CARRIAGE_RETURN,
    CHARACTER_TABULATION,
    COLON,
    COMMA,
    EQUALS_SIGN,
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
    QUOTATION_MARK,
    REVERSE_SOLIDUS,
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


def word_wrap(string):
    """
    INFORMATION_SEPARATOR_FOUR indicates end of file. Stop immediately.
    INFORMATION_SEPARATOR_THREE indicates end of line. Reset column.
    INFORMATION_SEPARATOR_TWO indicates punctuation. Break on long line.
    INFORMATION_SEPARATOR_ONE indicates whitespace. Break on long line.

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


def normalize_character(string):
    """
    Remove all invalid characters.
    """
    for character in string:
        if character in basic_multilingual_plane:
            yield from character


def normalize_whitespace(string):
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


def normalize_quotation(string):
    """"""

    for character in string:
        if character == QUOTATION_MARK:
            yield from APOSTROPHE
        else:
            yield from character


def normalize_punctuation(string):
    """"""

    previous = None
    for character in string:
        if character in unicode_punctuation:
            if character == previous:
                continue
        yield character
        previous = character


def normalize(string):
    """"""
    character = normalize_character(string)
    whitespace = normalize_whitespace(character)
    quotation = normalize_quotation(whitespace)
    punctuation = normalize_punctuation(quotation)
    yield from punctuation


def assignment_expression(identifier, expression):
    """
    Make a line for the file from a key value pair.
    return F'{identifier} = "{expression}"\n'
    """
    if not identifier.isidentifier():
        raise ValueError("Not a valid identifier.")
    if keyword.iskeyword(identifier):
        raise ValueError("This word is a keyword.")
    if keyword.issoftkeyword(identifier):
        raise ValueError("This word is a soft keyword.")

    yield from LINE_FEED
    yield from identifier
    yield from SPACE
    yield from EQUALS_SIGN
    yield from SPACE
    yield from QUOTATION_MARK
    yield from INFORMATION_SEPARATOR_FOUR
    yield from normalize(expression)
    yield from QUOTATION_MARK
    yield from LINE_FEED


def transverse_dictionary(dictionary):
    """"""
    items = dictionary.items()
    sorted_items = sorted(items)
    for key, value in sorted_items:
        yield from assignment_expression(key, value)


def dictionary_file(dictionary):
    """"""
    yield from QUOTATION_MARK
    yield from QUOTATION_MARK
    yield from QUOTATION_MARK
    yield from dictionary["LANGUAGE_TAG_ISO"]
    yield from SPACE
    yield from dictionary["LANGUAGE_NAME_ENGLISH"]
    yield from SPACE
    yield from dictionary["LANGUAGE_NAME_NATIVE"]
    yield from QUOTATION_MARK
    yield from QUOTATION_MARK
    yield from QUOTATION_MARK
    yield from LINE_FEED
    yield from transverse_dictionary(dictionary)


def dictionary_to_file(dictionary):
    """"""
    file = dictionary_file(dictionary)
    yield from word_wrap(file)
