"""Central place for loading and importing external files."""


import lzma

from celestine import load
from celestine.typed import (
    FILE,
    GS,
    LZMA,
    OS,
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


def binary(path: P, mode: S) -> FILE:
    """Does all file opperations."""
    encoding = None  # Binary mode doesn't take an 'encoding' argument.
    errors = None  #: Binary mode doesn't take an 'errors' argument
    return raw(path, mode, encoding, errors)


def binary_load(path: P) -> FILE:
    """"""
    return binary(path, READ_BINARY)


def binary_read(path: P) -> S:
    """"""
    with binary_load(path) as file:
        return file.read()


def binary_save(path: P) -> FILE:
    """"""
    return binary(path, WRITE_BINARY)


def binary_write(path: P, data: S) -> N:
    """"""
    with binary_save(path) as file:
        file.write(data)


def lzma_load(path: P) -> LZMA:
    """"""
    return lzma.open(
        path,
        mode=READ_BINARY,
    )


def lzma_read(path: P) -> S:
    """"""
    with lzma_load(path) as file:
        return file.read()


def lzma_save(path: P) -> LZMA:
    """"""
    return lzma.open(
        path,
        mode=WRITE_BINARY,
        format=lzma.FORMAT_XZ,
        check=lzma.CHECK_SHA256,
        preset=9,
        filters=None,
    )


def lzma_write(path: P, data: S) -> N:
    """"""
    with lzma_save(path) as file:
        file.write(bytes(data))


def raw(path: P, mode: S, encoding: OS, errors: OS) -> FILE:
    """Does all file opperations."""
    file = path
    buffering = 1  # Use line buffering.
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


def text(path: P, mode: S) -> FILE:
    """Does all file opperations."""
    encoding = UTF_8  # Use UTF 8 encoding.
    errors = STRICT  # Raise a ValueError exception on error.
    return raw(path, mode, encoding, errors)


def text_load(path: P) -> FILE:
    """"""
    return text(path, READ_TEXT)


def text_read(path: P) -> S:
    """"""
    with text_load(path) as file:
        return file.read()


def text_save(path: P) -> FILE:
    """"""
    return text(path, WRITE_TEXT)


def text_write(path: P, data: S) -> N:
    """"""
    with text_save(path) as file:
        file.write(data)


########################################################################


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
