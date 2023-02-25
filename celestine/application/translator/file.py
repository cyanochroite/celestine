"""Central place for loading and importing external files."""

from celestine import load
from celestine.application.translator.parser import dictionary_to_file
from celestine.text import stream


def save_string(string, *path):
    """Save a string to a file."""
    file = load.python(*path)
    mode = stream.WRITE_TEXT
    buffering = 1  # use line buffering
    encoding = stream.UTF_8
    errors = stream.STRICT
    newline = stream.UNIVERSAL
    closefd = True  # close file descriptor
    opener = None  # use default opener
    with open(
        file,
        mode,
        buffering,
        encoding,
        errors,
        newline,
        closefd,
        opener,
    ) as file_object:
        for character in string:
            file_object.write(character)


def save_dictionary(dictionary, *path):
    """Convert a dictionary to a string and save it to a file."""
    string = dictionary_to_file(dictionary)
    save_string(string, *path)
