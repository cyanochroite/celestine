"""Central place for loading and importing external files."""


import lzma

from celestine import load
from celestine.file import data as stream
from celestine.typed import (
    FILE,
    GS,
    LZMA,
    OS,
    N,
    P,
    S,
)


def binary(path: P, mode: S) -> FILE:
    """Does all file opperations."""
    encoding = None  # Binary mode doesn't take an 'encoding' argument.
    errors = None  #: Binary mode doesn't take an 'errors' argument
    return raw(path, mode, encoding, errors)


def binary_load(path: P) -> FILE:
    """"""
    return binary(path, stream.READ_BINARY)


def binary_read(path: P) -> S:
    """"""
    with binary_load(path) as file:
        return file.read()


def binary_save(path: P) -> FILE:
    """"""
    return binary(path, stream.WRITE_BINARY)


def binary_write(path: P, data: S) -> N:
    """"""
    with binary_save(path) as file:
        file.write(data)


def lzma_load(path: P) -> LZMA:
    """"""
    return lzma.open(
        path,
        mode=stream.READ_BINARY,
    )


def lzma_read(path: P) -> S:
    """"""
    with lzma_load(path) as file:
        return file.read()


def lzma_save(path: P) -> LZMA:
    """"""
    return lzma.open(
        path,
        mode=stream.WRITE_BINARY,
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
    newline = stream.UNIVERSAL  # Universal newlines mode.
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
    encoding = stream.UTF_8  # Use UTF 8 encoding.
    errors = stream.STRICT  # Raise a ValueError exception on error.
    return raw(path, mode, encoding, errors)


def text_load(path: P) -> FILE:
    """"""
    return text(path, stream.READ_TEXT)


def text_read(path: P) -> S:
    """"""
    with text_load(path) as file:
        return file.read()


def text_save(path: P) -> FILE:
    """"""
    return text(path, stream.WRITE_TEXT)


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
