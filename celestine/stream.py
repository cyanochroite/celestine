"""Central place for loading and importing external files."""

import abc
import enum
import lzma
import os
import pathlib
from typing import (
    IO,
    TextIO,
)

from celestine import load
from celestine.typed import (
    A,
    B,
    N,
    P,
    ignore,
    S,
    override,
)

type Flie = IO[A]
type Lzma = lzma.LZMAFile | TextIO
type Path = P | S

MAXIMUM_LINE_LENGTH = 72
SECTION_BREAK = "######################################################\
##################"


class Buffering(enum.IntEnum):
    """"""

    OFF = 0
    ON = 1


class Encoding(enum.StrEnum):
    """"""

    ASCII = "ascii"
    ISO_8859_1 = "iso_8859_1"
    LATIN_1 = "latin_1"
    US_ASCII = "us_ascii"
    UTF_8 = "utf_8"
    UTF_16 = "utf_16"
    UTF_32 = "utf_32"


class Errors(enum.StrEnum):
    """"""

    BACKSLASHREPLACE = "backslashreplace"
    IGNORE = "ignore"
    NAMEREPLACE = "namereplace"
    REPLACE = "replace"
    STRICT = "strict"
    SURROGATEESCAPE = "surrogateescape"
    XMLCHARREFREPLACE = "xmlcharrefreplace"


class Mode(enum.StrEnum):
    """"""

    APPEND_BINARY = "ab"
    APPEND_TEXT = "at"
    EXCLUSIVE_BINARY = "xb"
    EXCLUSIVE_TEXT = "xt"
    READ_BINARY = "rb"
    READ_TEXT = "rt"
    TRUNCATE_BINARY = "w+b"
    TRUNCATE_TEXT = "w+t"
    UPDATE_BINARY = "r+b"
    UPDATE_TEXT = "r+t"
    WRITE_BINARY = "wb"
    WRITE_TEXT = "wt"


class Newline(enum.StrEnum):
    """"""

    APPLE = "\n"
    COMMODORE = "\r"
    MICROSOFT = "\r\n"
    UNTRANSLATED = ""


class File(abc.ABC):
    """"""

    directory: P

    def _file(self, strict: B, *path: Path) -> P:
        root = self.directory

        join: S = os.path.join(root, *path)
        norm: S = os.path.normpath(join)
        real: S = os.path.realpath(norm, strict=strict)

        safe = os.path.commonpath((root, real))

        if not os.path.samefile(root, safe):
            raise RuntimeError()

        file = pathlib.Path(*path)
        return file

    def load(self, *path: Path) -> S:
        """"""
        with self.reader(*path) as file:
            return file.read()

    @abc.abstractmethod
    def reader(self, *path: Path) -> Flie:
        """"""
        ignore(self)
        ignore(path)
        raise NotImplementedError()

    def save(self, data: S, *path: Path) -> N:
        """"""
        with self.writer(*path) as file:
            file.write(data)

    @abc.abstractmethod
    def writer(self, *path: Path) -> Flie:
        """"""
        ignore(self)
        ignore(path)
        raise NotImplementedError()

    def __init__(self, path: P) -> N:
        self.directory = path


class Binary(File):
    """"""

    @override
    def reader(self, *path: Path) -> Flie:
        """"""
        return open(
            self._file(True, *path),
            Mode.READ_BINARY,
            Buffering.OFF,
        )

    @override
    def writer(self, *path: Path) -> Flie:
        """"""
        return open(
            self._file(False, *path),
            Mode.WRITE_BINARY,
            Buffering.OFF,
        )


class Compress(File):
    """"""

    @override
    def reader(self, *path: Path) -> Lzma:
        """"""
        return lzma.open(
            self._file(True, *path),
            Mode.READ_BINARY,
        )

    @override
    def writer(self, *path: Path) -> Lzma:
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
    def reader(self, *path: Path) -> Flie:
        """"""
        return open(
            self._file(True, *path),
            Mode.READ_TEXT,
            Buffering.ON,
            Encoding.UTF_8,
            Errors.STRICT,
        )

    @override
    def writer(self, *path: Path) -> Flie:
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
    def reader(self, *path: Path) -> Flie:
        """"""
        ignore(self)
        paths = list(map(str, path))
        file = load.python(*paths)
        return super().reader(file)

    @override
    def writer(self, *path: Path) -> Flie:
        """"""
        ignore(self)
        paths = list(map(str, path))
        file = load.python(*paths)
        return super().writer(file)


# set this in session loading.
directory = load.project_root()

project_root = load.project_root()
project_path = load.project_path()

binary = Binary(directory)
compress = Compress(directory)
module = Module(project_path)
text = Text(directory)
