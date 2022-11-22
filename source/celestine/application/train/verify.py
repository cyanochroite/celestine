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

    def write_smart(self, item, extra, last):
        size = len(item)
        if self.column + size + extra <= MAXIMUM_LINE_LENGTH:
            self.column += self.string.write(item)
            if not last:
                self.column += self.string.write(SPACE)
        else:
            self.column += self.string.write("\\")
            self.column += self.string.write(LINE_FEED)
            if self.column > MAXIMUM_LINE_LENGTH + 1:
                raise ValueError("Text overflowed maximum length.")
            self.column = 0
            #
            self.column += self.string.write(item)
            if not last:
                self.column += self.string.write(SPACE)

    def write_value(self, key, value):
        self.string = io.StringIO()
        self.column = 0
        self.column += self.string.write(key)
        self.column += self.string.write(SPACE)
        self.column += self.string.write(EQUALS_SIGN)
        self.column += self.string.write(SPACE)
        self.column += self.string.write(QUOTATION_MARK)
        key = ['fish', 'dog', 'frog']
        index = 0

        index = 0
        length = len(value) - 1
        while index < length:
            item = value[index]
            self.write_smart(item, 2, False)
            index += 1
        item = value[index]
        self.write_smart(item, 1, True)

        self.column += self.string.write(QUOTATION_MARK)
        self.column += self.string.write(LINE_FEED)
        result = self.string.getvalue()
        self.string.close()
        return result


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


def normalize(word):
    """
    Remove all whitespace characters.
    Preserve gaps between words.
    Only permit line breaks after punctuation.
    """
    string = io.StringIO()
    blank = 1
    letter = 2
    symbol = 3
    state = 0
    for line in word:
        if line in whitespace:
            if state == letter:
                state = blank
        elif line in punctuation:
            string.write(line)
            state = symbol
        else:
            if state == blank:
                string.write(SPACE)
            if state == symbol:
                string.write(BREAK_PERMITTED_HERE)
            string.write(line)
            state = letter
    value = string.getvalue()
    split = value.split(BREAK_PERMITTED_HERE)
    return split

#


cat = normalize(LANGUAGE)
file = File("name", "header", [])
car = file.write_value("cat", cat)
print(car)
item("cat", cat)

