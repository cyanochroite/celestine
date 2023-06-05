"""Central place for loading and importing external files."""


from celestine.typed import (
    GE,
    N,
    P,
    S,
)
from celestine.unicode import NONE

from . import data as stream


def context(file: P, mode: S) -> N:
    """Does all file opperations."""
    file = file
    mode = mode
    buffering = 1  # Use line buffering.
    encoding = stream.UTF_8  # Use UTF 8 encoding.
    errors = stream.STRICT  # Raise a ValueError exception on error.
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


def raw(file: P, mode: S, encoding, errors) -> N:
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


def context_binary(file: P, mode: S) -> N:
    """Does all file opperations."""
    file = file
    mode = mode
    encoding = None  # Binary mode doesn't take an encoding argument.
    errors = None  #: Binary mode doesn't take an errors argument
    return raw(file, mode, encoding, errors)


def open_binary_stream(file: P) -> GE[S, N, N]:
    """"""
    mode = stream.READ_BINARY
    with context_binary(file, mode) as document:
        yield from document


########################################################################


def text(file: P, mode: S) -> N:
    """Does all file opperations."""
    file = file
    mode = mode
    encoding = stream.UTF_8  # Use UTF 8 encoding.
    errors = stream.STRICT  # Raise a ValueError exception on error.
    return raw(file, mode, encoding, errors)


def text_open(file: P) -> GE[S, N, N]:
    """"""
    mode = stream.READ_TEXT
    with text(file, mode) as document:
        yield from document


def text_save(string: S, file: P) -> N:
    """"""
    mode = stream.WRITE_TEXT
    with text(file, mode) as document:
        for line in string:
            document.write(line)


def module_open(file: P) -> GE[S, N, N]:
    """"""
    mode = stream.READ_TEXT
    with text(file, mode) as document:
        yield from document


def module_save(string: S, *path: S) -> N:
    """"""
    file = NONE.join([pathway(*path), PYTHON_EXTENSION])
    text_save(string, file)
