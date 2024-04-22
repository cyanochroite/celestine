from celestine.application.viewer.parser.operator import (
    number_parse,
    tab_parse,
    unary_parse,
    word_parse,
)
from celestine.unicode.alphabet import (
    Comparison,
    Digit,
    Divider,
    Letter,
    Unary,
)
from celestine.unicode.encoding import encoding

from .operator import comparison_parse


def log_unicode(character, info):
    """"""
    message = "Unicode Character Code U+{0:04X}:'{1}' {2}"
    print(message.format(ord(character), character, info))


def decode(character):
    """"""
    item = encoding.get(character, False)

    if item is True:
        log_unicode(character, "Not Defined")
        return None

    if item is False:
        log_unicode(character, "Not Implemented")
        return None

    return item


def maps(iterable):
    """"""
    item = iterable[0]
    mapping = {
        Comparison: comparison_parse,
        Digit: number_parse,
        Divider: tab_parse,
        Letter: word_parse,
        Unary: unary_parse,
    }
    matt = mapping.get(type(item))
    cats = matt(iterable)
    return cats


class translator:  # translate
    """"""

    @staticmethod
    def translate(string):
        return filter(map(decode, string))


class tokenizer:
    """"""

    @staticmethod
    def tokenize(iterable):
        pass
        # TODO change to hold.package.itertools
        # TODO import from top of file?
        # return list(
        #    more_itertools.split_when(
        #        iterable, lambda x, y: type(x) is not type(y))
        # )


class parser:
    """"""

    @staticmethod
    def parse(iterable):
        return list(map(maps, iterable))
