"""Central place for loading and importing external files."""

import enum
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


class Binary:
    """"""

    @classmethod
    def load(cls, path: P) -> S:
        """"""
        with cls.reader(path) as file:
            return file.read()

    @classmethod
    def reader(cls, path: P) -> FILE:
        """"""
        return cls._open(path, Mode.READ_BINARY)

    @classmethod
    def save(cls, path: P, data: S) -> N:
        """"""
        with cls.writer(path) as file:
            file.write(data)

    @classmethod
    def writer(cls, path: P) -> FILE:
        """"""
        return cls._open(path, Mode.WRITE_BINARY)

    @classmethod
    def _open(cls, file: P, mode: Mode) -> FILE:
        """"""
        # Using open without explicitly specifying an encoding.
        # pylint: disable-next=W1514
        return open(
            file,
            mode,
            buffering=Buffering.OFF,
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
            mode=Mode.READ_BINARY,
        )

    def save(self, path: P, data: S) -> N:
        """"""
        with self.writer(path) as file:
            file.write(data)

    def writer(self, path: P) -> LZMA:
        """"""
        return lzma.open(
            path,
            mode=Mode.WRITE_BINARY,
            format=lzma.FORMAT_XZ,
            check=lzma.CHECK_SHA256,
            preset=9,
            filters=None,
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
    def reader(cls, path: P) -> FILE:
        """"""
        return cls._open(path, Mode.READ_TEXT)

    @classmethod
    def save(cls, path: P, data: S) -> N:
        """"""
        with cls.writer(path) as file:
            file.write(data)

    @classmethod
    def writer(cls, path: P) -> FILE:
        """"""
        return cls._open(path, Mode.WRITE_TEXT)

    @classmethod
    def _open(cls, file: P, mode: Mode) -> FILE:
        """"""
        return open(
            file,
            mode,
            buffering=Buffering.ON,
            encoding=Encoding.UTF_8,
            errors=Errors.STRICT,
        )
