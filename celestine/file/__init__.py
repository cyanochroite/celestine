"""Central place for loading and importing external files."""


from celestine import load
from celestine.typed import (
    GE,
    P,
    S,
    OS,
    N,
    FILE,
)

from . import data as stream


def binary(file: P, mode: S) -> FILE:
    """Does all file opperations."""
    encoding = None  # Binary mode doesn't take an encoding argument.
    errors = None  #: Binary mode doesn't take an errors argument
    return raw(file, mode, encoding, errors)


def binary_load(file: P) -> FILE:
    """"""
    return binary(file, stream.READ_BINARY)


def binary_save(file: P) -> FILE:
    """"""
    return binary(file, stream.WRITE_BINARY)


def raw(file: P, mode: S, encoding: OS, errors: OS) -> FILE:
    """Does all file opperations."""
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


def text(file: P, mode: S) -> FILE:
    """Does all file opperations."""
    encoding = stream.UTF_8  # Use UTF 8 encoding.
    errors = stream.STRICT  # Raise a ValueError exception on error.
    return raw(file, mode, encoding, errors)


def text_load(file: P) -> FILE:
    """"""
    return text(file, stream.READ_TEXT)


def text_save(file: P) -> FILE:
    """"""
    return text(file, stream.WRITE_TEXT)


########################################################################


def module_open(*path: S) -> GE[S, N, N]:
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
