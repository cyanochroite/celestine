"""Central place for loading and importing external files."""

import abc
import lzma
import os
import pathlib
import sys

from celestine import load
from celestine.typed import (
    FILE,
    LZMA,
    PATH,
    B,
    N,
    P,
    OP,
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

    directory: P

    def _file(self, strict: B, *path: PATH) -> P:
        root = self.directory

        join: S = os.path.join(root, *path)
        norm: S = os.path.normpath(join)
        real: S = os.path.realpath(norm, strict=strict)

        safe = os.path.commonpath((root, real))

        if not os.path.samefile(root, safe):
            raise RuntimeError()

        file = pathlib.Path(*path)
        return file

    def load(self, *path: PATH) -> S:
        """"""
        with self.reader(*path) as file:
            return file.read()

    @abc.abstractmethod
    def reader(self, *path: PATH) -> FILE:
        """"""

    def save(self, data: S, *path: PATH) -> N:
        """"""
        with self.writer(*path) as file:
            file.write(data)

    @abc.abstractmethod
    def writer(self, *path: PATH) -> FILE:
        """"""

    def __init__(self, path: P) -> N:
        self.directory = path


class Binary(File):
    """"""

    @override
    def reader(self, *path: PATH) -> FILE:
        """"""
        return open(
            self._file(True, *path),
            Mode.READ_BINARY,
            Buffering.OFF,
        )

    @override
    def writer(self, *path: PATH) -> FILE:
        """"""
        return open(
            self._file(False, *path),
            Mode.WRITE_BINARY,
            Buffering.OFF,
        )


class Compress(File):
    """"""

    @override
    def reader(self, *path: PATH) -> LZMA:
        """"""
        return lzma.open(
            self._file(True, *path),
            Mode.READ_BINARY,
        )

    @override
    def writer(self, *path: PATH) -> LZMA:
        """"""
        return lzma.open(
            self._file(False, *path),
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
        return open(
            self._file(True, *path),
            Mode.READ_TEXT,
            Buffering.ON,
            Encoding.UTF_8,
            Errors.STRICT,
        )

    @override
    def writer(self, *path: PATH) -> FILE:
        """"""
        return open(
            self._file(False, *path),
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


# set this in session loading.
directory = load.project_root()

project_root = load.project_root()
project_path = load.project_path()

binary = Binary(directory)
compress = Compress(directory)
module = Module(project_path)
text = Text(directory)
