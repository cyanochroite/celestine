"""Central place for loading and importing external files."""
import io
import keyword

from celestine.string.all import WRITE
from celestine.string.all import UTF_8

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
from celestine.string.unicode import NO_BREAK_HERE
from celestine.string.unicode import REVERSE_SOLIDUS

from celestine.string.unicode import NEXT_LINE

from celestine.string.unicode import LINE_SEPARATOR
from celestine.string.unicode import PARAGRAPH_SEPARATOR


MAXIMUM_LINE_LENGTH = 72
LINE_BUFFERING = 1
STRICT = "strict"
WRITE_TEXT = WRITE
CLOSE = True
OPENER = None

NONE = ""

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


LANGUAGE = "  В ЕС има 24\rофициални\nезика:\tанглийски, български,\
гръцки, 123 ' s , датски, естонски?, ? испански!, италиански,, латвийски, литовски, малтийски, немски, нидерландски, полски, португалски, румънски, словашки, словенски, унгарски, фински, френски, хърватски, чешки и шведски. m "


class File():
    """Write a key value pair python file."""

    def __init__(self, name, header, iterable):
        self.name = F"{name}.py"
        self.head = F'"""{header}"""\n'
        self.body = map(self.line, iterable)

        self.column = 0

    def savedf(self, path):
        """Save the items."""
        with open(path, WRITE, encoding=UTF_8) as file:
            file.write(self.head)
            file.writelines(self.body)

    def save(self, path, string):
        with open(path, WRITE_TEXT, LINE_BUFFERING, UTF_8, STRICT,
                  LINE_FEED, True, None) as file:
            for character in word_wrap(string):
                file.write(character)

    def save(self, path, string):
        with open(path, WRITE_TEXT, LINE_BUFFERING, UTF_8, STRICT,
                  LINE_FEED, True, None) as file:
            for character in string:
                file.write(character)

    @ staticmethod
    def line(item):
        """Make a line for the file from a key value pair."""
        (key, value) = item
        if not key.isidentifier():
            raise ValueError("Not a valid identifier.")
        if keyword.iskeyword(key) or keyword.issoftkeyword(key):
            raise ValueError("This word is a keyword.")
        value = value.replace('"', "'")
        return F'{key} = "{value}"\n'


def word_wrap(text):
    line = text.split(BREAK_PERMITTED_HERE)

    column = 0

    for item in line:
        size = len(item)

        if column + size >= MAXIMUM_LINE_LENGTH:
            yield REVERSE_SOLIDUS
            yield LINE_FEED
            column = 0

        yield item
        column += size


def buffer_readline(buffer):
    buffer.write(CARRIAGE_RETURN)
    buffer.seek(0, io.SEEK_SET)
    string = buffer.readline()
    for character in string:
        if character == LINE_SEPARATOR:
            yield LINE_FEED
        elif character != CARRIAGE_RETURN:
            yield character
    buffer.seek(0, io.SEEK_SET)


def word_wrap(string):
    buffer = io.StringIO(NONE, CARRIAGE_RETURN)

    column = 0
    size = 0

    for character in string:
        if character == BREAK_PERMITTED_HERE:

            if column + size >= MAXIMUM_LINE_LENGTH:
                yield REVERSE_SOLIDUS
                yield LINE_FEED
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
                yield SPACE
                yield BREAK_PERMITTED_HERE
            elif previous in unicode_identifier:
                if whitespace:
                    yield SPACE

        whitespace = character in unicode_whitespace

        if not whitespace:
            yield character
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

    yield identifier
    yield SPACE
    yield EQUALS_SIGN
    yield SPACE
    yield QUOTATION_MARK
    yield BREAK_PERMITTED_HERE
    yield from normalize_whitespace(expression)
    yield QUOTATION_MARK
    yield LINE_SEPARATOR


def work(value):
    string = io.StringIO()

    for item2 in value:
        string.write(item2)

    string.seek(0, io.SEEK_SET)

    while True:
        line = string.readline()

        if not line:
            break

        yield from word_wrap(line)

    string.close()


def testaa():
    string2 = io.StringIO()

    gofish = {
        "A": "B",
        "fast_train": LANGUAGE,
        "choo_choo": LANGUAGE,
        "language": LANGUAGE,
        "dancing": LANGUAGE,
        "dancer": LANGUAGE,
    }

    for (key, value) in gofish.items():
        cow = assignment_expression(key, value)
        pig = work(cow)
        for item in pig:
            string2.write(item)

    cat = string2.getvalue()

    string2.close()

    print(cat)


testaa()
A = "B"
fast_train = "В ЕС има 24 официални езика: английски, български, \
гръцки, 123's, датски, естонски?,? испански!, италиански,, латвийски, \
литовски, малтийски, немски, нидерландски, полски, португалски, \
румънски, словашки, словенски, унгарски, фински, френски, хърватски, \
чешки и шведски. m"
choo_choo = "В ЕС има 24 официални езика: английски, български, \
гръцки, 123's, датски, естонски?,? испански!, италиански,, латвийски, \
литовски, малтийски, немски, нидерландски, полски, португалски, \
румънски, словашки, словенски, унгарски, фински, френски, хърватски, \
чешки и шведски. m"
language = "В ЕС има 24 официални езика: английски, български, гръцки, \
123's, датски, естонски?,? испански!, италиански,, латвийски, \
литовски, малтийски, немски, нидерландски, полски, португалски, \
румънски, словашки, словенски, унгарски, фински, френски, хърватски, \
чешки и шведски. m"
dancing = "В ЕС има 24 официални езика: английски, български, гръцки, \
123's, датски, естонски?,? испански!, италиански,, латвийски, \
литовски, малтийски, немски, нидерландски, полски, португалски, \
румънски, словашки, словенски, унгарски, фински, френски, хърватски, \
чешки и шведски. m"
dancer = "В ЕС има 24 официални езика: английски, български, гръцки, \
123's, датски, естонски?,? испански!, италиански,, латвийски, \
литовски, малтийски, немски, нидерландски, полски, португалски, \
румънски, словашки, словенски, унгарски, фински, френски, хърватски, \
чешки и шведски. m"
