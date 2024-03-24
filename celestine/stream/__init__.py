"""Central place for loading and importing external files."""

import abc
import lzma
import pathlib

from celestine import load
from celestine.typed import (
    FILE,
    LZMA,
    PATH,
    N,
    P,
    S,
    override,
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


class File(abc.ABC):
    """"""

    def load(self, *path: PATH) -> S:
        """"""
        with self.reader(*path) as file:
            return file.read()

    @abc.abstractmethod
    def reader(self, *path: PATH) -> FILE:
        ...

    def save(self, data: S, *path: PATH) -> N:
        """"""
        with self.writer(*path) as file:
            file.write(data)

    @abc.abstractmethod
    def writer(self, *path: PATH) -> FILE:
        ...

    def join(self, *path: PATH) -> P:
        """"""
        return pathlib.Path(*path)


class Binary(File):
    """"""

    @override
    def reader(self, *path: PATH) -> FILE:
        """"""
        file = self.join(*path)
        return open(
            file,
            Mode.READ_BINARY,
            Buffering.OFF,
        )

    @override
    def writer(self, *path: PATH) -> FILE:
        """"""
        file = self.join(*path)
        return open(
            file,
            Mode.WRITE_BINARY,
            Buffering.OFF,
        )


class Lzma(File):
    """"""

    @override
    def reader(self, *path: PATH) -> LZMA:
        """"""
        file = self.join(*path)
        return lzma.open(
            file,
            Mode.READ_BINARY,
        )

    @override
    def writer(self, *path: PATH) -> LZMA:
        """"""
        file = self.join(*path)
        return lzma.open(
            file,
            Mode.WRITE_BINARY,
            format=lzma.FORMAT_XZ,
            check=lzma.CHECK_SHA256,
            preset=9,
        )


class Text(File):
    """"""

    @override
    def reader(self, *path: PATH) -> FILE:
        """"""
        file = self.join(*path)
        return open(
            file,
            Mode.READ_TEXT,
            Buffering.ON,
            Encoding.UTF_8,
            Errors.STRICT,
        )

    @override
    def writer(self, *path: PATH) -> FILE:
        """"""
        file = self.join(*path)
        return open(
            file,
            Mode.WRITE_TEXT,
            Buffering.ON,
            Encoding.UTF_8,
            Errors.STRICT,
        )


class Module(Text):
    """"""

    @override
    def reader(self, *path: PATH) -> FILE:
        """"""
        file = load.python(*path)
        super().reader(file)

    @override
    def writer(self, *path: PATH) -> FILE:
        """"""
        file = load.python(*path)
        super().writer(file)


binary = Binary()
module = Module()
text = Text()
