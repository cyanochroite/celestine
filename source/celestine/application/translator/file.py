"""Central place for loading and importing external files."""

from celestine.text import stream


def save(path, string):
    file = path
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
