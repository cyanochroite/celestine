"""Central place for loading and importing external files."""

import io

from celestine import load
from celestine.data import stream
from celestine.typed import (
    GE,
    N,
    P,
    S,
)


def read_stream(lines: GE[S, N, N]) -> S:
    string = io.StringIO()
    for line in lines:
        string.write(line)
    value = string.getvalue()
    return value


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


def open_file(file: P) -> S:
    """"""
    stream = open_file_stream(file)
    return read_stream(stream)


def open_file_stream(file: P) -> GE[S, N, N]:
    """"""
    mode = stream.READ_TEXT
    with context(file, mode) as document:
        yield from document


def open_module(*path: S) -> S:
    """"""
    stream = open_module_stream(file)
    return read_stream(stream)


def open_module_stream(file: P) -> GE[S, N, N]:
    """"""
    mode = stream.READ_TEXT
    with context(file, mode) as document:
        yield from document


def save_file(string: S, file: P) -> N:
    """"""
    mode = stream.WRITE_TEXT
    with context(file, mode) as document:
        for line in string:
            document.write(line)


def save_module(string: S, *path: S) -> N:
    """"""
    file = load.python(*path)
    save_file(string, file)
