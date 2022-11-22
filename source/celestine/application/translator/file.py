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
гръцки, 123, датски, естонски?, ? испански!, италиански,, латвийски, литовски, малтийски, немски, нидерландски, полски, португалски, румънски, словашки, словенски, унгарски, фински, френски, хърватски, чешки и шведски. m "


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


class Character(enum.Enum):
    IDENTIFIER = enum.auto()
    NONE = enum.auto()
    PUNCTUATION = enum.auto()
    WHITESPACE = enum.auto()


symbol = {
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


def normalize(word):
    """
    Remove all whitespace characters.
    Preserve gaps between words.
    Only permit line breaks after punctuation.
    """
    string = io.StringIO()
    state = Character.NONE
    for line in word:
        if line in whitespace:
            if state == Character.IDENTIFIER:
                state = Character.WHITESPACE
        elif line in punctuation:
            string.write(line)
            state = Character.PUNCTUATION
        else:
            if state == Character.WHITESPACE:
                string.write(SPACE)
            if state == Character.PUNCTUATION:
                string.write(BREAK_PERMITTED_HERE)
            string.write(line)
            state = Character.IDENTIFIER
    value = string.getvalue()
    split = value.split(BREAK_PERMITTED_HERE)
    return split

#


def normalize(word):
    """
    Remove all whitespace characters.
    Preserve gaps between words.
    Only permit line breaks after punctuation.
    """
    string = io.StringIO()
    state = Character.NONE
    for line in word:
        match symbol.get(line, Character.IDENTIFIER):
            case Character.IDENTIFIER:
                match state:
                    case Character.PUNCTUATION:
                        string.write(BREAK_PERMITTED_HERE)
                    case Character.WHITESPACE:
                        string.write(SPACE)
                string.write(line)
                state = Character.IDENTIFIER
            case Character.PUNCTUATION:
                string.write(line)
                state = Character.PUNCTUATION
            case Character.WHITESPACE:
                match state:
                    case Character.IDENTIFIER:
                        state = Character.WHITESPACE
    value = string.getvalue()
    split = value.split(BREAK_PERMITTED_HERE)
    return split


def normalize(word):
    """
    Remove all whitespace characters.
    Preserve gaps between words.
    Only permit line breaks after punctuation.
    """
    string = io.StringIO()
    state = Character.NONE
    for line in word:
        hat = symbol.get(line, Character.IDENTIFIER)
        match (hat, state):
            case (Character.WHITESPACE, Character.IDENTIFIER):
                state = Character.WHITESPACE
            case (Character.PUNCTUATION, *_):
                string.write(line)
                state = Character.PUNCTUATION
            case (Character.IDENTIFIER, Character.PUNCTUATION):
                string.write(BREAK_PERMITTED_HERE)
                string.write(line)
                state = Character.IDENTIFIER
            case (Character.IDENTIFIER, Character.WHITESPACE):
                string.write(SPACE)
                string.write(line)
                state = Character.IDENTIFIER
    value = string.getvalue()
    split = value.split(BREAK_PERMITTED_HERE)
    return split

# global test


def write_value(string, key, value):
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


def normalize(string, word):
    """
    Remove all whitespace characters.
    Preserve gaps between words.
    Only permit line breaks after punctuation.
    """
    state = Character.NONE
    for line in word:
        match symbol.get(line, Character.IDENTIFIER):
            case Character.IDENTIFIER:
                match state:
                    case Character.PUNCTUATION:
                        string.write(BREAK_PERMITTED_HERE)
                    case Character.WHITESPACE:
                        string.write(SPACE)
                string.write(line)
                state = Character.IDENTIFIER
            case Character.PUNCTUATION:
                string.write(line)
                state = Character.PUNCTUATION
            case Character.WHITESPACE:
                match state:
                    case Character.IDENTIFIER:
                        state = Character.WHITESPACE

# string = io.StringIO()
# cat = normalize(string, LANGUAGE)
# value = string.getvalue()
# split = value.split(BREAK_PERMITTED_HERE)

# car = write_value(string, "cat", split)
# result = string.getvalue()
# string.close()


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


def write_value(key, value):
    string = io.StringIO()

    string.write(key)
    string.write(SPACE)
    string.write(EQUALS_SIGN)
    string.write(SPACE)

    string.write(QUOTATION_MARK)

    for item in value:
        string.write(item)

    string.write(QUOTATION_MARK)
    string.write(LINE_FEED)

    value = string.getvalue()
    split = value.split(BREAK_PERMITTED_HERE)

    string.close()
    return split


def normalize_whitespace(word):
    """
    Remove all whitespace characters.
    Preserve gaps between words.
    Only permit line breaks after punctuation.
    """
    state = Character.NONE
    for line in word:
        match symbol.get(line, Character.IDENTIFIER):
            case Character.IDENTIFIER:
                match state:
                    case Character.PUNCTUATION:
                        yield BREAK_PERMITTED_HERE
                    case Character.WHITESPACE:
                        yield NO_BREAK_HERE
                yield line
                state = Character.IDENTIFIER
            case Character.PUNCTUATION:
                yield line
                state = Character.PUNCTUATION
            case Character.WHITESPACE:
                match state:
                    case Character.IDENTIFIER:
                        state = Character.WHITESPACE


def normalize(word):
    """
    Remove all whitespace characters.
    Preserve gaps between words.
    Only permit line breaks after punctuation.
    """
    state = Character.NONE
    for line in word:
        if line in punctuation:
            yield line
            state = Character.PUNCTUATION
        elif line == SPACE:
            match state:
                case Character.IDENTIFIER:
                    state = Character.WHITESPACE
        else:
            match state:
                case Character.PUNCTUATION:
                    yield BREAK_PERMITTED_HERE
                case Character.WHITESPACE:
                    yield NO_BREAK_HERE
            yield line
            state = Character.IDENTIFIER


def normalize(word):
    """
    Remove all whitespace characters.
    Preserve gaps between words.
    Only permit line breaks after punctuation.
    """
    state = Character.NONE
    for line in word:
        if line in punctuation:
            yield line
            state = Character.PUNCTUATION
        elif line == SPACE:
            match state:
                case Character.IDENTIFIER:
                    state = Character.WHITESPACE
        else:
            match state:
                case Character.PUNCTUATION:
                    yield BREAK_PERMITTED_HERE
                case Character.WHITESPACE:
                    yield NO_BREAK_HERE
            yield line
            state = Character.IDENTIFIER


def normalize_whitespace(string):
    for character in string:
        yield SPACE if character in whitespace else character


def normalize_whitespace(string):
    previous = False
    for character in string:
        current = character != SPACE
        if current or previous:
            yield character
        previous = current


def whitespace_collapse(string):
    """
    Remove all consecutive whitespace characters.
    Return a copy of the string with the leading
    and trailing whitespace characters removed.
    """
    previous = False
    for character in string:
        current = character != SPACE
        if current:
            if not previous:
                yield SPACE
            yield character
        previous = current


def normalize_whitespace(string):
    """
    All whitespace characters become spaces.
    Remove all consecutive whitespace characters.
    Return a copy of the string with the leading
    and trailing whitespace characters removed.
    """
    previous = False
    for character in string:
        current = character not in whitespace
        if current:
            if not previous:
                yield SPACE
            yield character
        previous = current


#
zero = LANGUAGE
one = normalize_whitespace(zero)
two = normalize(one)

car = write_value("cat", two)

print(car)
