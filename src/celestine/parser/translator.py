from celestine.encoding.u0000 import u0000
from celestine.encoding.u0080 import u0080
from celestine.encoding.u2700 import u2700


encoding = u0000 | u0080 | u2700


class translator():
    @staticmethod
    def translate(string):
        array = []
        for character in string:
            item = encoding.get(character)
            if item is None:
                log.Warning("NO CHAATER")
            else:
                array.append(item)
        return str().join(array)
