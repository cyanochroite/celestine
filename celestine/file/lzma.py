"""Central place for loading and importing external files."""

import lzma

from celestine.file.data import (
    READ_BINARY,
    WRITE_BINARY,
)
from celestine.typed import (
    FILE,
    LZMA,
    N,
    P,
    S,
)


class Funny:
    """"""

    def load(self, path: P) -> S:
        """"""
        with self.reader(path) as file:
            return file.read()

    def reader(self, path: P) -> FILE:
        """"""
        return binary(path, READ_BINARY)

    def save(self, path: P, data: S) -> N:
        """"""
        with self.writer(path) as file:
            file.write(data)

    def writer(self, path: P) -> FILE:
        """"""
        return binary(path, WRITE_BINARY)

    def __init__(self) -> N:
        self.encoding = (
            None  # Binary mode doesn't take an 'encoding' argument.
        )
        self.errors = (
            None  #: Binary mode doesn't take an 'errors' argument
        )


class Binary(Funny):
    """"""

    def reader(self, path: P) -> LZMA:
        """"""
        return lzma.open(
            path,
            mode=READ_BINARY,
        )

    def save(self, path: P, data: S) -> N:
        """"""
        with self.writer(path) as file:
            file.write(bytes(data))

    def writer(self, path: P) -> LZMA:
        """"""
        return lzma.open(
            path,
            mode=WRITE_BINARY,
            format=lzma.FORMAT_XZ,
            check=lzma.CHECK_SHA256,
            preset=9,
            filters=None,
        )

    def __init__(self) -> N:
        self.encoding = (
            None  # Binary mode doesn't take an 'encoding' argument.
        )
        self.errors = (
            None  #: Binary mode doesn't take an 'errors' argument
        )
