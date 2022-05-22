from celestine.data.encoding import encoding
from celestine.core.text import log


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
        array = []
        for character in string:
            item = encoding.get(character)
            if item is None:
                log_unicode(item, "Not Found")
            else:
                array.append(item)
        return [item for item in array]

    @staticmethod
    def translate(string):
        return [item for item in map(decode, string) if item is not None]

class converter():
    @staticmethod
    def translate(iterable):
        # insert "end of input" signal
        iterable.append(None)
        inner = []
        outer = []
        mode = None
        for item in iterable:
            kind = type(item)
            if kind != mode:
                mode = kind
                outer.append(inner)
                inner = []
            inner.append(item)
        return [item for item in outer if item]
