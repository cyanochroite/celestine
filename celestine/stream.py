"""Central place for loading and importing external files."""

import importlib.resources
import io
import lzma as _lzma

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

# encoding
ASCII = "ascii"
ISO_8859_1 = "iso_8859_1"
LATIN_1 = "latin_1"
US_ASCII = "us_ascii"
UTF_8 = "utf_8"
UTF_16 = "utf_16"
UTF_32 = "utf_32"

# errors
BACKSLASHREPLACE = "backslashreplace"
IGNORE = "ignore"
NAMEREPLACE = "namereplace"
REPLACE = "replace"
STRICT = "strict"
SURROGATEESCAPE = "surrogateescape"
XMLCHARREFREPLACE = "xmlcharrefreplace"

# mode
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

# newline
APPLE = "\n"
COMMODORE = "\r"
MICROSOFT = "\r\n"
UNIVERSAL = None
UNTRANSLATED = ""


def module_open(*path: S) -> GS:
    """"""
    file = load.pathway.python(*path)
    with text_load(file) as document:
        yield from document


def module_save(string: S, *path: S) -> N:
    """"""
    file = load.pathway.python(*path)
    with text_save(file) as document:
        for line in string:
            document.write(line)


class File:
    """"""

    def load(self, path: P) -> S:
        """"""
        with self.reader(path) as file:
            return file.read()

    def reader(self, path: P) -> FILE:
        """"""
        return self._work(path, self.read)

    def save(self, path: P, data: S) -> N:
        """"""
        with self.writer(path) as file:
            file.write(data)

    def _work(self, path: P, mode: S) -> FILE:
        """Does all file opperations."""
        file = path
        buffering = 1  # Use line buffering.
        encoding = self.encoding
        errors = self.errors
        newline = UNIVERSAL  # Universal newlines mode.
        closefd = True  # The close file descriptor must be True.
        opener = None  # Use the default opener.
        return open(
            file,
            mode,
            buffering,
            encoding,
            errors,
            newline,
            closefd,
            opener,
        )

    def writer(self, path: P) -> FILE:
        """"""
        return self._work(path, self.write)

    def __init__(self, encoding, errors, read, write) -> N:
        self.encoding = encoding
        self.errors = errors
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
        return _lzma.open(
            path,
            mode=READ_BINARY,
        )

    def save(self, path: P, data: S) -> N:
        """"""
        with self.writer(path) as file:
            file.write(data)

    def writer(self, path: P) -> LZMA:
        """"""
        return _lzma.open(
            path,
            mode=WRITE_BINARY,
            format=_lzma.FORMAT_XZ,
            check=_lzma.CHECK_SHA256,
            preset=9,
            filters=None,
        )


class Resource:
    """"""

    def load(self, path: P) -> S:
        """"""
        with self.reader(path) as file:
            return file.read()

    def binary(self, child: S) -> io.TextIOWrapper:
        return self.reader(child, READ_BINARY)

    def text(self, child: S) -> io.TextIOWrapper:
        return self.reader(child, READ_TEXT)

    def reader(self, child: S, mode: S) -> io.TextIOWrapper:
        """"""
        files = importlib.resources.files(CELESTINE)
        traversable = files.joinpath(child)
        return traversable.open(
            mode=mode,
            buffering=1,  # Use line buffering.
            encoding=UTF_8,  # Use UTF 8 encoding.
            errors=STRICT,  # Raise a ValueError exception on error.
            newline=UNIVERSAL,  # Universal newlines mode.
        )


resource = Resource()


binary = File(
    None,  # Binary mode doesn't take an 'encoding' argument.
    None,  # Binary mode doesn't take an 'errors' argument.
    READ_BINARY,
    WRITE_BINARY,
)

text = File(
    UTF_8,  # Use UTF 8 encoding.
    STRICT,  # Raise a ValueError exception on error.
    READ_TEXT,
    WRITE_TEXT,
)

lzma = Lzma()
