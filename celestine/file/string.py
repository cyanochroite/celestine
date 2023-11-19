""""""

import io

from celestine.typed import (
    I,
    N,
    S,
)


class TextBuilder:
    """"""

    count: I
    text: io.StringIO

    def read(self) -> S:
        """"""
        self.text.seek(0, io.SEEK_SET)
        text = self.text.read(self.count)
        self.text.seek(0, io.SEEK_SET)
        self.count = 0
        return text

    def write(self, text: S) -> N:
        """"""
        self.count += self.text.write(text)

    def __init__(self) -> N:
        self.count = 0
        self.text = io.StringIO()


class Text:
    """"""

    text: S

    def __init__(self, *characters: S) -> N:
        builder = TextBuilder()
        for character in characters:
            builder.write(character)
        self.text = builder.read()

    def __str__(self) -> S:
        return self.text


def string(*characters: S) -> N:
    """"""
    buffer = io.StringIO()
    for character in characters:
        buffer.write(character)
    value = buffer.getvalue()
    return value
