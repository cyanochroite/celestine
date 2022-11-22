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
            if state != Character.WHITESPACE:
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
    """
    All whitespace characters become spaces.
    Remove all consecutive whitespace characters.
    Return a copy of the string with the leading
    and trailing whitespace characters removed.
    """
    previous_is_whitespace = False
    for character in string:
        current_not_whitespace = character not in whitespace
        if current_not_whitespace:
            if previous_is_whitespace:
                yield SPACE
            yield character
        previous_is_whitespace = not current_not_whitespace


def add_whitespace(string):
    """
    All whitespace characters become spaces.
    Remove all consecutive whitespace characters.
    Return a copy of the string with the leading
    and trailing whitespace characters removed.
    """
    previous_is_identifier = None
    previous_is_punctuation = None
    current_is_identifier = None
    current_is_punctuation = None
    for character in string:
        current_not_whitespace = character not in whitespace
        if current_not_whitespace:
            if previous_is_whitespace:
                yield SPACE
            yield character
        previous_is_whitespace = not current_not_whitespace


def add_whitespace(string):
    """
    All whitespace characters become spaces.
    Remove all consecutive whitespace characters.
    Return a copy of the string with the leading
    and trailing whitespace characters removed.
    """
    previous_is_punctuation = None
    current_is_punctuation = None
    for character in string:
        current_is_punctuation = character in punctuation
        if current_not_whitespace:
            if previous_is_whitespace:
                yield SPACE
            yield character
        previous_is_whitespace = not current_not_whitespace


def normalize(word):
    """
    Remove all whitespace characters.
    Preserve gaps between words.
    Only permit line breaks after punctuation.
    """
    state = Character.NONE
    for line in word:
        if line in punctuation:
            if state != Character.WHITESPACE:
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


def normalize_whitespace2(string):
    """
    All whitespace characters become spaces.
    Remove all consecutive whitespace characters.
    Return a copy of the string with the leading
    and trailing whitespace characters removed.
    """
    current_is_whitespace = character in whitespace
    current_is_alpha = character in whitespace
    current_is_punch = character in whitespace
    current = Character.NONE
    previous = Character.NONE
    found_whitespace = False
    for character in string:
        if current_is_whitespace:
            found_whitespace = True
        if current_is_punch:
            yield character
            state = Character.PUNCTUATION
            found_whitespace = False
        if current_is_alpha:
            if state == Character.PUNCTUATION:
                yield BREAK_PERMITTED_HERE
            elif state == Character.WHITESPACE:
                yield NO_BREAK_HERE
            yield character

            state = Character.IDENTIFIER
            found_whitespace = False

        else:
            is_it_a_letter = character in punctuation
            if not previous:
                yield SPACE
            yield character
            was_it_a_letter = is_it_a_letter
        previous_was_whitespace = current_is_whitespace
        previous_was_alpha = current_is_alpha
        previous_was_punch = current_is_punch


def normalize(word):
    """
    Remove all whitespace characters.
    Preserve gaps between words.
    Only permit line breaks after punctuation.
    """
    state = Character.NONE
    for line in word:
        if line in punctuation:
            if state != Character.WHITESPACE:
                yield line
            state = Character.PUNCTUATION
        elif line in whitespace:
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


class Insert(enum.Enum):
    BREAK_PERMITTED_HERE = enum.auto()
    CHARACTER = enum.auto()
    NO_BREAK_HERE = enum.auto()
    WHITESPACE = enum.auto()


class Character(enum.Enum):
    IDENTIFIER = enum.auto()
    NONE = enum.auto()
    PUNCTUATION = enum.auto()
    WHITESPACE = enum.auto()


def magic():
    character = yield
    state = Character.NONE
    while True:
        if character in punctuation:
            match state:
                case Character.IDENTIFIER:
                    character = yield Insert.CHARACTER
                case Character.NONE:
                    character = yield Insert.CHARACTER
                case Character.PUNCTUATION:
                    character = yield Insert.CHARACTER
                case Character.WHITESPACE:
                    pass
            state = Character.PUNCTUATION
        elif character in whitespace:
            match state:
                case Character.IDENTIFIER:
                    state = Character.WHITESPACE
                case Character.NONE:
                    character = yield Insert.WHITESPACE
                case Character.PUNCTUATION:
                    character = yield Insert.WHITESPACE
                case Character.WHITESPACE:
                    character = yield Insert.WHITESPACE
        else:
            match state:
                case Character.IDENTIFIER:
                    character = yield Insert.CHARACTER
                case Character.NONE:
                    character = yield Insert.CHARACTER
                case Character.PUNCTUATION:
                    character = yield Insert.BREAK_PERMITTED_HERE
                case Character.WHITESPACE:
                    character = yield Insert.NO_BREAK_HERE
            state = Character.IDENTIFIER


def normalize(string):
    check = magic()
    check.send(None)
    for character in string:
        match check.send(character):
            case Insert.CHARACTER:
                yield character
            case Insert.BREAK_PERMITTED_HERE:
                #                yield BREAK_PERMITTED_HERE
                yield "_"
                yield character
            case Insert.NO_BREAK_HERE:
                #                yield NO_BREAK_HERE
                yield "-"
                yield character
    check.close()


#
zero = LANGUAGE
one = normalize_whitespace(zero)
two = normalize(one)

dog = normalize(LANGUAGE)
string = io.StringIO()
for item in dog:
    string.write(item)

cat = string.getvalue()
car = write_value("cat", two)

print(car)
