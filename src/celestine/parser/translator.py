from celestine.data.encoding import encoding
from celestine.core.text import log

from celestine.package.itertools import split_when

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


class translator():
    @staticmethod
    def translate(string):
        return [item for item in map(decode, string) if item is not None]

class converter():
    @staticmethod
    def translate(iterable):
        return split_when(iterable, lambda x, y: type(x) is not type(y))
