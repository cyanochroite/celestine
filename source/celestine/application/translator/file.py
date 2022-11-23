"""Central place for loading and importing external files."""
import enum
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

from celestine.string.unicode import NEXT_LINE

from celestine.string.unicode import LINE_SEPARATOR
from celestine.string.unicode import PARAGRAPH_SEPARATOR


class File():
    """Write a key value pair python file."""

    def __init__(self, name, header, iterable):
        self.name = F"{name}.py"
        self.head = F'"""{header}"""\n'
        self.body = map(self.line, iterable)

        self.column = 0

    def save(self, path):
        """Save the items."""
        with open(path, WRITE, encoding=UTF_8) as file:
            file.write(self.head)
            file.writelines(self.body)

    @staticmethod
    def line(item):
        """Make a line for the file from a key value pair."""
        (key, value) = item
        if not key.isidentifier():
            raise ValueError("Not a valid identifier.")
        if keyword.iskeyword(key) or keyword.issoftkeyword(key):
            raise ValueError("This word is a keyword.")
        value = value.replace('"', "'")
        return F'{key} = "{value}"\n'


MAXIMUM_LINE_LENGTH = 72


LANGUAGE = "  В ЕС има 24\rофициални\nезика:\tанглийски, български,\
гръцки, 123 ' s , датски, естонски?, ? испански!, италиански,, латвийски, литовски, малтийски, немски, нидерландски, полски, португалски, румънски, словашки, словенски, унгарски, фински, френски, хърватски, чешки и шведски. m "


punctuation = [
    COLON,
    COMMA,
    EXCLAMATION_MARK,
    FULL_STOP,
    QUESTION_MARK,
    SEMICOLON,
]

whitespace = [
    CARRIAGE_RETURN,
    CHARACTER_TABULATION,
    FORM_FEED,
    INFORMATION_SEPARATOR_FOUR,
    INFORMATION_SEPARATOR_THREE,
    INFORMATION_SEPARATOR_TWO,
    LINE_FEED,
    LINE_SEPARATOR,
    LINE_SEPARATOR,
    LINE_TABULATION,
    NEXT_LINE,
    PARAGRAPH_SEPARATOR,
    SPACE,
]

apostrophe = [
    APOSTROPHE,
]


def write_value(key, value):
    string = io.StringIO()
    column = 0
    column += string.write(key)
    column += string.write(SPACE)
    column += string.write(EQUALS_SIGN)
    column += string.write(SPACE)

    column += string.write(QUOTATION_MARK)

    index = 0
    length = len(value) - 1

    extra = 2
    last = True

    while True:
        test = index < length

        if not test:
            extra = 1
            last = False

        item = value[index]
        size = len(item)
        if column + size + extra <= MAXIMUM_LINE_LENGTH:
            column += string.write(item)
            if not last:
                column += string.write(SPACE)
        else:
            column += string.write("\\")
            column += string.write(LINE_FEED)
            if column > MAXIMUM_LINE_LENGTH + 1:
                raise ValueError("Text overflowed maximum length.")
            column = 0
            #
            column += string.write(item)
            if not last:
                column += string.write(SPACE)
        index += 1
        if not test:
            break

    column += string.write(QUOTATION_MARK)
    column += string.write(LINE_FEED)
    result = string.getvalue()
    string.close()
    return result


class Insert(enum.Enum):
    BREAK_PERMITTED_HERE = enum.auto()
    CHARACTER = enum.auto()
    NO_BREAK_HERE = enum.auto()
    WHITESPACE = enum.auto()


class Character(enum.Enum):
    APOSTROPHE = enum.auto()
    IDENTIFIER = enum.auto()
    NONE = enum.auto()
    PUNCTUATION = enum.auto()
    WHITESPACE = enum.auto()


symbol = {
    APOSTROPHE: Character.APOSTROPHE,
    CARRIAGE_RETURN: Character.WHITESPACE,
    CHARACTER_TABULATION: Character.WHITESPACE,
    COLON: Character.PUNCTUATION,
    COMMA: Character.PUNCTUATION,
    EXCLAMATION_MARK: Character.PUNCTUATION,
    FORM_FEED: Character.WHITESPACE,
    FULL_STOP: Character.PUNCTUATION,
    INFORMATION_SEPARATOR_FOUR: Character.WHITESPACE,
    INFORMATION_SEPARATOR_THREE: Character.WHITESPACE,
    INFORMATION_SEPARATOR_TWO: Character.WHITESPACE,
    LINE_FEED: Character.WHITESPACE,
    LINE_SEPARATOR: Character.WHITESPACE,
    LINE_SEPARATOR: Character.WHITESPACE,
    LINE_TABULATION: Character.WHITESPACE,
    NEXT_LINE: Character.WHITESPACE,
    PARAGRAPH_SEPARATOR: Character.WHITESPACE,
    QUESTION_MARK: Character.PUNCTUATION,
    SEMICOLON: Character.PUNCTUATION,
    SPACE: Character.WHITESPACE,
    None: Character.NONE,
}


def write_line(string, key, value):
    column = 0
    column += string.write(key)
    column += string.write(SPACE)
    column += string.write(EQUALS_SIGN)
    column += string.write(SPACE)

    column += string.write(QUOTATION_MARK)

    index = 0
    length = len(value) - 1

    extra = 2
    last = True

    while True:
        test = index < length

        if not test:
            extra = 1
            last = False

        item = value[index]
        size = len(item)
        if column + size + extra <= MAXIMUM_LINE_LENGTH:
            column += string.write(item)
            if not last:
                column += string.write(SPACE)
        else:
            column += string.write("\\")
            column += string.write(LINE_FEED)
            if column > MAXIMUM_LINE_LENGTH + 1:
                raise ValueError("Text overflowed maximum length.")
            column = 0
            #
            column += string.write(item)
            if not last:
                column += string.write(SPACE)
        index += 1
        if not test:
            break

    column += string.write(QUOTATION_MARK)
    column += string.write(LINE_FEED)

#########


def write_line(text):
    string = io.StringIO()

    value = text.replace(NO_BREAK_HERE, SPACE)
    line = value.split(BREAK_PERMITTED_HERE)

    not_first = False
    column = 0
    for item in line:
        if not_first:
            column += string.write(SPACE)

        size = len(item) + len(SPACE)

        if column + size >= MAXIMUM_LINE_LENGTH:
            column += string.write("\\")
            column += string.write(LINE_FEED)
            if column > MAXIMUM_LINE_LENGTH + len(LINE_FEED):
                raise ValueError("Text overflowed maximum length.")
            column = 0

        column += string.write(item)
        not_first = True

    alldone = string.getvalue()
    string.close()
    return alldone


def assignment(key, value):
    yield key
    yield SPACE
    yield EQUALS_SIGN
    yield SPACE
    yield QUOTATION_MARK

    for item in value:
        yield item

    yield QUOTATION_MARK
    yield LINE_FEED


a = ["(", "<"]
b = [")", ">"]
c = ["!", "."]
d = ["'"]
e = []
f = []


def magic():
    character = yield
    state = Character.NONE
    white_people = False
    while True:
        value = symbol.get(character, Character.IDENTIFIER)
        match value:
            case Character.APOSTROPHE:
                character = yield Insert.CHARACTER
            case Character.IDENTIFIER:
                match state:
                    case Character.PUNCTUATION:
                        character = yield Insert.BREAK_PERMITTED_HERE
                    case Character.NONE:
                        character = yield Insert.CHARACTER
                    case Character.IDENTIFIER:
                        if white_people:
                            character = yield Insert.NO_BREAK_HERE
                        else:
                            character = yield Insert.CHARACTER
            case Character.PUNCTUATION:
                character = yield Insert.CHARACTER
            case _:
                character = yield Insert.WHITESPACE
        if value == Character.WHITESPACE:
            white_people = True
        else:
            white_people = False
            state = value


def normalize(string):
    check = magic()
    check.send(None)
    for character in string:
        match check.send(character):
            case Insert.CHARACTER:
                yield character
            case Insert.BREAK_PERMITTED_HERE:
                yield BREAK_PERMITTED_HERE
                yield character
            case Insert.NO_BREAK_HERE:
                yield NO_BREAK_HERE
                yield character
    check.close()


#

def work(value):
    string = io.StringIO()

    for item2 in value:
        string.write(item2)

    string.seek(0, io.SEEK_SET)

    while True:
        line = string.readline()

        if not line:
            break

        yield write_line(line)

    string.close()


string2 = io.StringIO()

gofish = {
    "language": LANGUAGE,
    "choo_choo": LANGUAGE,
    "finish": LANGUAGE,
    "oink": LANGUAGE,
}

for (go, fish) in gofish.items():
    moo = normalize(fish)
    cow = assignment(go, moo)
    pig = work(cow)
    for item in pig:
        string2.write(item)

cat = string2.getvalue()

string2.close()

print(cat)


