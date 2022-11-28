"""Central place for loading and importing external files."""
import io
import keyword

from celestine.string import stream

from celestine.application.translator.parser import word_wrap_dictionary


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
        mode = stream.WRITE_TEXT
        buffering = 1
        encoding = stream.UTF_8
        errors = stream.STRICT
        newline = stream.LINE_FEED
        closefd = True
        opener = None

        with open(path, mode, buffering, encoding,
                  errors, newline, closefd, opener) as file:
            for character in string:
                file.write(character)

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


def testab(string):
    string2 = io.StringIO()

    for item in string:
        string2.write(item)

    cat = string2.getvalue()

    string2.close()

    print(cat)


def testaa():
    dictionary = {
        "A": "B",
        "fast_train": LANGUAGE,
        "choo_choo": LANGUAGE,
        "language": LANGUAGE,
        "dancing": LANGUAGE,
        "dancer": LANGUAGE,
    }
    testab(word_wrap_dictionary(dictionary))


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
