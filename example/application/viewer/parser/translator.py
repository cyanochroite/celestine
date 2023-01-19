from celestine.data.encoding import encoding

from celestine.extension.more_itertools import split_when
from celestine.extension.more_itertools import filter_true


from celestine.data.alphabet import Comparison
from celestine.data.alphabet import Digit
from celestine.data.alphabet import Divider
from celestine.data.alphabet import Letter
from celestine.data.alphabet import Unary


from celestine.parser.operator import comparison_parse
from celestine.parser.operator import number_parse
from celestine.parser.operator import tab_parse
from celestine.parser.operator import word_parse
from celestine.parser.operator import unary_parse


def log_unicode(character, info):
    message = "Unicode Character Code U+{0:04X}:'{1}' {2}"
    print(message.format(ord(character), character, info))


def decode(character):
    item = encoding.get(character, False)

    if item is True:
        log_unicode(character, "Not Defined")
        return None

    if item is False:
        log_unicode(character, "Not Implemented")
        return None

    return item


def maps(iterable):
    item = iterable[0]
    mapping = {
        Comparison: comparison_parse,
        Digit: number_parse,
        Divider: tab_parse,
        Letter: word_parse,
        Unary: unary_parse
    }
    matt = mapping.get(type(item))
    cats = matt(iterable)
    return cats


class translator():  # translate
    @staticmethod
    def translate(string):
        return filter_true(map(decode, string))


class tokenizer():
    @staticmethod
    def tokenize(iterable):
        return list(split_when(iterable, lambda x, y: type(x) is not type(y)))


class parser():
    @staticmethod
    def parse(iterable):
        return list(map(maps, iterable))
