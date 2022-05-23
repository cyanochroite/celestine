from celestine.data.encoding import encoding
from celestine.core.text import log

from celestine.package.itertools import split_when
from celestine.package.itertools import filter_true


from celestine.data.alphabet import Comparison
from celestine.data.alphabet import Digit
from celestine.data.alphabet import Divider
from celestine.data.alphabet import Letter
from celestine.data.alphabet import Unary


from celestine.tag.operator import comparison_parse
from celestine.tag.operator import number_parse
from celestine.tag.operator import tab_parse
from celestine.tag.operator import word_parse
from celestine.tag.operator import unary_parse



def log_unicode(character, info):
    message = "Unicode Character Code U+{0:04X}:'{1}' {2}"
    log.warning(message.format(ord(character), character, info))


def decode(character):
    item = encoding.get(character, False)

    if item is True:
        log_unicode(character, "Not Found")
        return None

    if item is False:
        log_unicode(character, "Not Mapped")
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
    
class translator(): # translate
    @staticmethod
    def translate(string):
        return filter_true(map(decode, string))

class tokenizer():
    @staticmethod
    def tokenize(iterable):
        return split_when(iterable, lambda x, y: type(x) is not type(y))

class parser():
    @staticmethod
    def parse(iterable):
        return map(maps, iterable)
