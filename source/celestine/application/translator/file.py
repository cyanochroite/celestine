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
from celestine.string.unicode import REVERSE_SOLIDUS

from celestine.string.unicode import NEXT_LINE

from celestine.string.unicode import LINE_SEPARATOR
from celestine.string.unicode import PARAGRAPH_SEPARATOR


MAXIMUM_LINE_LENGTH = 72


LANGUAGE = "  В ЕС има 24\rофициални\nезика:\tанглийски, български,\
гръцки, 123 ' s , датски, естонски?, ? испански!, италиански,, латвийски, литовски, малтийски, немски, нидерландски, полски, португалски, румънски, словашки, словенски, унгарски, фински, френски, хърватски, чешки и шведски. m "


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
}


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


def write_line(text):
    line = text.split(BREAK_PERMITTED_HERE)

    column = 0

    for item in line:
        size = len(item)

        if column + size >= MAXIMUM_LINE_LENGTH:
            yield REVERSE_SOLIDUS
            yield LINE_FEED
            column = 0

        column += size
        yield item


def assignment(key, value):
    """
    Make a line for the file from a key value pair.
    return F'{key} = "{value}"\n'
    """
    if not key.isidentifier():
        raise ValueError("Not a valid identifier.")
    if keyword.iskeyword(key) or keyword.issoftkeyword(key):
        raise ValueError("This word is a keyword.")

    yield key
    yield SPACE
    yield EQUALS_SIGN
    yield SPACE
    yield QUOTATION_MARK
    yield BREAK_PERMITTED_HERE

    for item in value:
        yield item

    yield QUOTATION_MARK
    yield LINE_FEED


def magic():
    character = None
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
                yield SPACE
                yield BREAK_PERMITTED_HERE
                yield character
            case Insert.NO_BREAK_HERE:
                yield SPACE
                yield character
    check.close()


#


def normalize(string):
    state = Character.NONE
    white_people = False

    for character in string:
        value = symbol.get(character, Character.IDENTIFIER)
        match value:
            case Character.IDENTIFIER:
                match state:
                    case Character.PUNCTUATION:
                        yield SPACE
                        yield BREAK_PERMITTED_HERE
                    case Character.IDENTIFIER:
                        if white_people:
                            yield SPACE

        if value != Character.WHITESPACE and value != Character.NONE:
            yield character

        if value == Character.WHITESPACE:
            white_people = True
        else:
            white_people = False
            state = value


def normalize(string):
    state = Character.NONE
    whitespace = False

    for character in string:
        value = symbol.get(character, Character.IDENTIFIER)
        if value == Character.IDENTIFIER:
            match state:
                case Character.PUNCTUATION:
                    yield SPACE
                    yield BREAK_PERMITTED_HERE
                case Character.IDENTIFIER:
                    if whitespace:
                        yield SPACE

        whitespace = value == Character.WHITESPACE
        if not whitespace:
            yield character
            state = value

####


apostrophe = frozenset({
    APOSTROPHE,
})

punctuation = frozenset({
    COLON,
    COMMA,
    EXCLAMATION_MARK,
    FULL_STOP,
    QUESTION_MARK,
    SEMICOLON,
})

whitespace = frozenset({
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
})

plane_0 = set({})
for index in range(0x10000):
    plane_0.add(chr(index))

basic_multilingual_plane = frozenset(plane_0)

not_identifier = apostrophe | punctuation | whitespace

identifier = basic_multilingual_plane - not_identifier


def normalize(string):
    state = Character.NONE
    white_space = False
    last = APOSTROPHE

    for character in string:
        if character not in not_identifier:
            value = symbol.get(last, Character.IDENTIFIER)
            state = value
            match state:
                case Character.PUNCTUATION:
                    yield SPACE
                    yield BREAK_PERMITTED_HERE
                case Character.IDENTIFIER:
                    if white_space:
                        yield SPACE

        value = symbol.get(character, Character.IDENTIFIER)
        white_space = value == Character.WHITESPACE
        if not white_space:
            yield character
            last = character


def normalize(string):
    white_space = False
    last = APOSTROPHE

    for character in string:
        if character in identifier:
            if last in punctuation:
                yield SPACE
                yield BREAK_PERMITTED_HERE
            elif last in identifier:
                if white_space:
                    yield SPACE

        value = symbol.get(character, Character.IDENTIFIER)
        white_space = value == Character.WHITESPACE
        if not white_space:
            yield character
            last = character


class Characteuuieir(enum.Enum):
    NONE = enum.auto()
    WHITESPACE = enum.auto()
    APOSTROPHE = enum.auto()


asymbol = [
    APOSTROPHE,
    CARRIAGE_RETURN,
    CHARACTER_TABULATION,
    COLON,
    COMMA,
    EXCLAMATION_MARK,
    FORM_FEED,
    FULL_STOP,
    INFORMATION_SEPARATOR_FOUR,
    INFORMATION_SEPARATOR_THREE,
    INFORMATION_SEPARATOR_TWO,
    LINE_FEED,
    LINE_SEPARATOR,
    LINE_SEPARATOR,
    LINE_TABULATION,
    NEXT_LINE,
    PARAGRAPH_SEPARATOR,
    QUESTION_MARK,
    SEMICOLON,
    SPACE,
]


def anormalize(string):
    state = Character.WHITESPACE
    whitespace = False

    for character in string:
        if character not in symbol:
            match state:
                case Character.PUNCTUATION:
                    yield SPACE
                    yield BREAK_PERMITTED_HERE
                case Character.IDENTIFIER:
                    if whitespace:
                        yield SPACE

        whitespace = value == Character.WHITESPACE
        if not whitespace:
            yield character
            state = value


def work(value):
    string = io.StringIO()

    for item2 in value:
        string.write(item2)

    string.seek(0, io.SEEK_SET)

    while True:
        line = string.readline()

        if not line:
            break

        yield from write_line(line)

    string.close()


def testaa():
    string2 = io.StringIO()

    gofish = {
        "cho_choSch": LANGUAGE,
        "choo_choo": LANGUAGE,
        "language": LANGUAGE,
        "dancing": LANGUAGE,
        "dancer": LANGUAGE,
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


testaa()

cho_choSch = "В ЕС има 24 официални езика: английски, български, \
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
