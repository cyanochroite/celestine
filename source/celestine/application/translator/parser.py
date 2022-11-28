"""Central place for loading and importing external files."""
import io
import keyword


from celestine.string.unicode import NONE

from celestine.string.unicode import EQUALS_SIGN
from celestine.string.unicode import LINE_FEED
from celestine.string.unicode import QUOTATION_MARK
from celestine.string.unicode import SPACE


from celestine.string.unicode import FULL_STOP
from celestine.string.unicode import QUESTION_MARK
from celestine.string.unicode import EXCLAMATION_MARK
from celestine.string.unicode import COMMA
from celestine.string.unicode import SEMICOLON
from celestine.string.unicode import COLON

from celestine.string.unicode import APOSTROPHE


from celestine.string.unicode import CHARACTER_TABULATION
from celestine.string.unicode import LINE_TABULATION
from celestine.string.unicode import FORM_FEED
from celestine.string.unicode import CARRIAGE_RETURN


from celestine.string.unicode import INFORMATION_SEPARATOR_FOUR
from celestine.string.unicode import INFORMATION_SEPARATOR_THREE
from celestine.string.unicode import INFORMATION_SEPARATOR_TWO

from celestine.string.unicode import BREAK_PERMITTED_HERE
from celestine.string.unicode import REVERSE_SOLIDUS

from celestine.string.unicode import NEXT_LINE

from celestine.string.unicode import LINE_SEPARATOR
from celestine.string.unicode import PARAGRAPH_SEPARATOR


MAXIMUM_LINE_LENGTH = 72


unicode_apostrophe = frozenset({
    APOSTROPHE,
})

unicode_punctuation = frozenset({
    COLON,
    COMMA,
    EXCLAMATION_MARK,
    FULL_STOP,
    QUESTION_MARK,
    SEMICOLON,
})

unicode_whitespace = frozenset({
    CARRIAGE_RETURN,
    CHARACTER_TABULATION,
    FORM_FEED,
    INFORMATION_SEPARATOR_FOUR,
    INFORMATION_SEPARATOR_THREE,
    INFORMATION_SEPARATOR_TWO,
    LINE_FEED,
    LINE_SEPARATOR,
    LINE_TABULATION,
    NEXT_LINE,
    PARAGRAPH_SEPARATOR,
    SPACE,
})

plane_0 = set({})
for index in range(0x10000):
    plane_0.add(chr(index))

basic_multilingual_plane = frozenset(plane_0)

not_identifier = set({})
not_identifier |= unicode_apostrophe
not_identifier |= unicode_punctuation
not_identifier |= unicode_whitespace

unicode_identifier = basic_multilingual_plane - not_identifier


def buffer_readline(buffer):
    buffer.write(CARRIAGE_RETURN)
    buffer.seek(0, io.SEEK_SET)
    string = buffer.readline()
    for character in string:
        if character == LINE_SEPARATOR:
            yield from LINE_FEED
        elif character != CARRIAGE_RETURN:
            yield from character
    buffer.seek(0, io.SEEK_SET)


def word_wrap(string):
    """
    Lines will be MAXIMUM_LINE_LENGTH unless no breaks detected.
    Use BREAK_PERMITTED_HERE to signal a soft line break.
    Use LINE_SEPARATOR to signal a hard line break.
    Do not use LINE_FEED or CARRIAGE_RETURN as weird things may happen.
    BREAK_PERMITTED_HERE will be removed from the string.
    LINE_SEPARATOR will be replaced with LINE_FEED.
    """
    buffer = io.StringIO(NONE, CARRIAGE_RETURN)

    column = 0
    size = 0

    for character in string:

        if character == LINE_SEPARATOR:
            if column + size > MAXIMUM_LINE_LENGTH:
                yield from LINE_FEED

            yield from buffer_readline(buffer)
            yield from LINE_FEED

            column = 0
            size = 0

        elif character == BREAK_PERMITTED_HERE:

            if column + size + 1 > MAXIMUM_LINE_LENGTH:
                yield from REVERSE_SOLIDUS
                yield from LINE_FEED
                column = 0

            yield from buffer_readline(buffer)

            column += size
            size = 0

        else:
            buffer.write(character)
            size += 1

    yield from buffer_readline(buffer)


def normalize_whitespace(string):
    """
    Trim whitespace from ends.
    Convert all whitespace to spaces.
    Remove all duplicate spaces.
    Preserve space between words.
    Ensure space after every punctuation.
    Remove space before punctuation.
    Allow line breaks after punctuation.
    """
    previous = None
    whitespace = None

    for character in string:
        if character in unicode_identifier:
            if previous in unicode_punctuation:
                yield from SPACE
                yield from BREAK_PERMITTED_HERE
            elif previous in unicode_identifier:
                if whitespace:
                    yield from SPACE

        whitespace = character in unicode_whitespace

        if not whitespace:
            yield from character
            previous = character


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

    yield from identifier
    yield from SPACE
    yield from EQUALS_SIGN
    yield from SPACE
    yield from QUOTATION_MARK
    yield from BREAK_PERMITTED_HERE
    yield from normalize_whitespace(expression)
    yield from QUOTATION_MARK
    yield from LINE_SEPARATOR


def transverse_dictionary(dictionary):
    for (key, value) in dictionary.items():
        yield from assignment_expression(key, value)


def word_wrap_dictionary(dictionary):
    yield from word_wrap(transverse_dictionary(dictionary))
