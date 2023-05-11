"""Central place for loading and importing external files."""

from celestine import load
from celestine.application.translator.parser import dictionary_to_file
from celestine.text import stream
from celestine.typed import (
    GE,
    N,
    P,
    S,
)


def open_object(file: P, mode: S) -> None:
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


def open_file(file: P) -> GE[S, N, N]:
    """"""
    mode = stream.READ_TEXT
    with open_object(file, mode) as document:
        yield from document


def open_module(*path: S) -> GE[S, N, N]:
    """"""
    file = load.python(*path)
    yield from open_file(file)


def save_file(string: S, file: P) -> N:
    """"""
    mode = stream.WRITE_TEXT
    with open_object(file, mode) as document:
        for line in string:
            document.write(line)


def save_module(string: S, *path: S) -> N:
    """"""
    file = load.python(*path)
    save_file(string, file)


def save_dictionary(dictionary, *path):
    """Convert a dictionary to a string and save it to a file."""
    string = dictionary_to_file(dictionary)
    save_module(string, *path)
