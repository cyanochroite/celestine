from celestine.data.encoding import encoding


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
        value = [item.value for item in array]
        return str().join(value)
