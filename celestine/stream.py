"""Central place for loading and importing external files."""

import importlib.resources
import io
import lzma
import enum

from celestine import load
from celestine.data import CELESTINE
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


class Buffering(enum.Enum):
    """"""
    OFF = 0
    ON = 1


class Encoding(enum.Enum):
    """"""
    ASCII = "ascii"
    ISO_8859_1 = "iso_8859_1"
    LATIN_1 = "latin_1"
    NONE = None
    US_ASCII = "us_ascii"
    UTF_8 = "utf_8"
    UTF_16 = "utf_16"
    UTF_32 = "utf_32"


class Errors(enum.Enum):
    """"""
    BACKSLASHREPLACE = "backslashreplace"
    IGNORE = "ignore"
    NAMEREPLACE = "namereplace"
    NONE = None
    REPLACE = "replace"
    STRICT = "strict"
    SURROGATEESCAPE = "surrogateescape"
    XMLCHARREFREPLACE = "xmlcharrefreplace"


class Mode(enum.Enum):
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


class Newline(enum.Enum):
    """"""
    APPLE = "\n"
    COMMODORE = "\r"
    MICROSOFT = "\r\n"
    UNIVERSAL = None
    UNTRANSLATED = ""


class File:
    """"""

    buffering: Buffering
    encoding: Encoding
    errors: Errors
    newline: Newline
    read: Mode
    write: Mode

    def load(self, path: P) -> S:
        """"""
        with self.reader(path) as file:
            return file.read()

    def reader(self, path: P) -> FILE:
        """"""
        return self._open(path, self.read)

    def save(self, path: P, data: S) -> N:
        """"""
        with self.writer(path) as file:
            file.write(data)

    def writer(self, path: P) -> FILE:
        """"""
        return self._open(path, self.write)

    def _open(self, file: P, mode: Mode) -> FILE:
        """Does all file opperations."""
        return open(
            file,
            mode.value,
            buffering=self.buffering.value,
            encoding=self.encoding.value,
            errors=self.errors.value,
            newline=self.newline.value,
            closefd=True,
            opener=None,
        )

    def __init__(
        self,
        buffering: Buffering,
        encoding: Encoding,
        errors: Errors,
        newline: Newline,
        read: Mode,
        write: Mode,
    ) -> N:
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.read = read
        self.write = write


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
            mode=Mode.READ_BINARY.value,
        )

    def save(self, path: P, data: S) -> N:
        """"""
        with self.writer(path) as file:
            file.write(data)

    def writer(self, path: P) -> LZMA:
        """"""
        return lzma.open(
            path,
            mode=Mode.WRITE_BINARY.value,
            format=lzma.FORMAT_XZ,
            check=lzma.CHECK_SHA256,
            preset=9,
            filters=None,
        )


class Module:
    """"""

    def load(self, *paths: S) -> GS:
        """"""
        path = load.python(*paths)
        with text.reader(path) as file:
            yield from file

    def save(self, string: GS, *paths: S) -> N:
        """"""
        path = load.python(*paths)
        with text.writer(path) as file:
            for line in string:
                file.write(line)


compression = Lzma()

binary = File(
    Buffering.OFF,
    Encoding.NONE,
    Errors.NONE,
    Newline.UNIVERSAL,
    Mode.READ_BINARY,
    Mode.WRITE_BINARY,
)

text = File(
    Buffering.ON,
    Encoding.UTF_8,
    Errors.STRICT,
    Newline.UNIVERSAL,
    Mode.READ_TEXT,
    Mode.WRITE_TEXT,
)

module = Module()
