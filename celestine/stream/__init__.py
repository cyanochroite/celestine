"""Central place for loading and importing external files."""

import lzma

from celestine import load
from celestine.typed import (
    FILE,
    GS,
    LZMA,
    N,
    P,
    S,
)

from .data import (
    Buffering,
    Encoding,
    Errors,
    Mode,
)

MAXIMUM_LINE_LENGTH = 72
SECTION_BREAK = "######################################################\
##################"


class Binary:
    """"""

    @classmethod
    def load(cls, path: P) -> S:
        """"""
        with cls.reader(path) as file:
            return file.read()

    @classmethod
    def reader(cls, file: P) -> FILE:
        """"""
        return open(
            file,
            Mode.READ_BINARY,
            Buffering.OFF,
        )

    @classmethod
    def save(cls, path: P, data: S) -> N:
        """"""
        with cls.writer(path) as file:
            file.write(data)

    @classmethod
    def writer(cls, file: P) -> FILE:
        """"""
        return open(
            file,
            Mode.WRITE_BINARY,
            Buffering.OFF,
        )


class Lzma:
    """"""

    def load(self, path: P) -> S:
        """"""
        with self.reader(path) as file:
            return file.read()

    def reader(self, path: P) -> LZMA:
        """"""
        return lzma.open(
            path,
            Mode.READ_BINARY,
        )

    def save(self, path: P, data: S) -> N:
        """"""
        with self.writer(path) as file:
            file.write(data)

    def writer(self, path: P) -> LZMA:
        """"""
        return lzma.open(
            path,
            Mode.WRITE_BINARY,
            format=lzma.FORMAT_XZ,
            check=lzma.CHECK_SHA256,
            preset=9,
        )


class Module:
    """"""

    @classmethod
    def load(cls, *paths: S) -> GS:
        """"""
        path = load.python(*paths)
        with Text.reader(path) as file:
            yield from file

    @classmethod
    def save(cls, string: GS, *paths: S) -> N:
        """"""
        path = load.python(*paths)
        with Text.writer(path) as file:
            for line in string:
                file.write(line)


class Text:
    """"""

    @classmethod
    def load(cls, path: P) -> S:
        """"""
        with cls.reader(path) as file:
            return file.read()

    @classmethod
    def reader(cls, file: P) -> FILE:
        """"""
        return open(
            file,
            Mode.READ_TEXT,
            Buffering.ON,
            Encoding.UTF_8,
            Errors.STRICT,
        )

    @classmethod
    def save(cls, path: P, data: S) -> N:
        """"""
        with cls.writer(path) as file:
            file.write(data)

    @classmethod
    def writer(cls, file: P) -> FILE:
        """"""
        return open(
            file,
            Mode.WRITE_TEXT,
            Buffering.ON,
            Encoding.UTF_8,
            Errors.STRICT,
        )
