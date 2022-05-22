from celestine.data.encoding import encoding
from celestine.data.alphabet import More
from celestine.core.text import log

def log_unicode(character, info):
    message = "Unicode Character Code U+{0:04X}:'{1}' {2}"
    log.warning(message.format(ord(character), character, info))


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


class converter():
    @staticmethod
    def translate(array):
        inner = []
        outer = []
        mode = None
        for item in array:
            kind = type(item)
            if kind != mode:
                mode = kind
                if inner:
                    outer.append(inner)
                inner = []
            if item is More.NONE:
                log_unicode(item.value, "Not Mapped")
            else:
                inner.append(item)
        if inner:
            outer.append(inner)
        return outer
