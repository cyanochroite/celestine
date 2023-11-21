"""Central place for loading and importing external files."""


from celestine.file import (
    READ_BINARY,
    READ_TEXT,
    STRICT,
    UTF_8,
    WRITE_BINARY,
    WRITE_TEXT,
    raw,
)
from celestine.typed import (
    FILE,
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
