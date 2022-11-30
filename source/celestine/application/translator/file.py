"""Central place for loading and importing external files."""

from celestine.string import stream


class File():
    """Write a key value pair python file."""

    def __init__(self, name, header):
        self.name = F"{name}.py"
        self.head = F'"""{header}"""\n'

    def save(self, path, string):
        mode = stream.WRITE_TEXT
        buffering = 1
        encoding = stream.UTF_8
        errors = stream.STRICT
        newline = stream.UNIVERSAL
        closefd = True
        opener = None

        with open(path, mode, buffering, encoding,
                  errors, newline, closefd, opener) as file:
            for character in string:
                file.write(character)
