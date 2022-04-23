from celestine.tag.alphabet import convert


class translator():
    @staticmethod
    def translate(string):
        return str().join(
            [
                item for item in
                [convert.get(character) for character in string]
                if item is not None
            ]
        )
