"""Central place for loading and importing external files."""
import re
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


from celestine.string.unicode import SPACE
from celestine.string.unicode import CHARACTER_TABULATION
from celestine.string.unicode import LINE_FEED
from celestine.string.unicode import LINE_TABULATION
from celestine.string.unicode import FORM_FEED
from celestine.string.unicode import CARRIAGE_RETURN


from celestine.string.unicode import LINE_FEED
from celestine.string.unicode import CARRIAGE_RETURN
from celestine.string.unicode import LINE_TABULATION
from celestine.string.unicode import FORM_FEED

from celestine.string.unicode import INFORMATION_SEPARATOR_FOUR
from celestine.string.unicode import INFORMATION_SEPARATOR_THREE
from celestine.string.unicode import INFORMATION_SEPARATOR_TWO
from celestine.string.unicode import INFORMATION_SEPARATOR_ONE  # unused?

from celestine.string.unicode import NEXT_LINE

from celestine.string.unicode import LINE_SEPARATOR
from celestine.string.unicode import PARAGRAPH_SEPARATOR

import string
car = string.punctuation


class File():
    """Write a key value pair python file."""

    def __init__(self, name, header, iterable):
        self.name = F"{name}.py"
        self.head = F'"""{header}"""\n'
        self.body = map(self.line, iterable)

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
гръцки, датски, естонски?, ? испански!, италиански,, латвийски, литовски, малтийски, немски, нидерландски, полски, португалски, румънски, словашки, словенски, унгарски, фински, френски, хърватски, чешки и шведски. m "


punctuation = [
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
    LINE_SEPARATOR,
    LINE_TABULATION,
    NEXT_LINE,
    PARAGRAPH_SEPARATOR,
    QUESTION_MARK,
    SEMICOLON,
    SPACE,
]

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
    INFORMATION_SEPARATOR_ONE,
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
    Convert all whitespace to spaces.
    Remove all spaces around punctuation.
    Ensure all words have a space before them if preceeded by a word
    or punctuation.
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
                string.write(SPACE)
            string.write(line)
            state = letter
    value = string.getvalue()
    return value


special = str().join(punctuation)
search = F"([{special}]+)"
pattern = re.compile(search)
repl = r"<\1>"

hold = str().join(whitespace)
search = F"[{hold}]+"

output = re.sub(
    search,
    SPACE,
    LANGUAGE,
)

hold = str().join(punctuation)
search = F"(\S)*([{punctuation}]+)(\S*)"

output = re.sub(
    search,
    r'\2',
    LANGUAGE,
)

output = re.sub(pattern, repl, LANGUAGE)

print(output)

cat = normalize(LANGUAGE)


def item():
    string = io.StringIO()
    key = "a"
    value = "b"
    column = 0
    column += string.write(key)
    column += string.write(SPACE)
    column += string.write(EQUALS_SIGN)
    column += string.write(SPACE)
    column += string.write(QUOTATION_MARK)
    column += string.write(value)
    column += string.write(QUOTATION_MARK)
    column += string.write(LINE_FEED)
    print(column)
    cat = string.getvalue()
    print(string.getvalue())
    print("cowbo")
    car = string
    string.close()


