"""Central place for loading and importing external files."""


from celestine.stream.data import (
    READ_BINARY,
    READ_TEXT,
    STRICT,
    UNIVERSAL,
    UTF_8,
    WRITE_BINARY,
    WRITE_TEXT,
)
from celestine.typed import (
    FILE,
    OS,
    N,
    P,
    S,
)


class Funny:
    """"""

    def raw(self, path: P, mode: S, encoding: OS, errors: OS) -> FILE:
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

    def load(self, path: P) -> S:
        """"""
        with self.reader(path) as file:
            return file.read()

    def reader(self, path: P) -> FILE:
        """"""
        return self.work(path, READ_BINARY)

    def save(self, path: P, data: S) -> N:
        """"""
        with self.writer(path) as file:
            file.write(data)

    def writer(self, path: P) -> FILE:
        """"""
        return self.work(path, WRITE_BINARY)

    def work(self, path: P, mode: S) -> FILE:
        """Does all file opperations."""
        encoding = (
            None  # Binary mode doesn't take an 'encoding' argument.
        )
        errors = None  #: Binary mode doesn't take an 'errors' argument
        return self.raw(path, mode, encoding, errors)


class Binary(Funny):
    """"""

    def work(self, path: P, mode: S) -> FILE:
        """Does all file opperations."""
        encoding = (
            None  # Binary mode doesn't take an 'encoding' argument.
        )
        errors = None  #: Binary mode doesn't take an 'errors' argument
        return self.raw(path, mode, encoding, errors)

    def reader(self, path: P) -> FILE:
        """"""
        return self.work(path, READ_BINARY)

    def writer(self, path: P) -> FILE:
        """"""
        return self.work(path, WRITE_BINARY)

    def __init__(self) -> N:
        self.encoding = (
            None  # Binary mode doesn't take an 'encoding' argument.
        )
        self.errors = (
            None  #: Binary mode doesn't take an 'errors' argument
        )


class Text(Funny):
    """"""

    def work(self, path: P, mode: S) -> FILE:
        """Does all file opperations."""
        encoding = UTF_8  # Use UTF 8 encoding.
        errors = STRICT  # Raise a ValueError exception on error.
        return self.raw(path, mode, encoding, errors)

    def reader(self, path: P) -> FILE:
        """"""
        return self.work(path, READ_TEXT)

    def writer(self, path: P) -> FILE:
        """"""
        return self.work(path, WRITE_TEXT)

    def __init__(self) -> N:
        encoding = UTF_8  # Use UTF 8 encoding.
        errors = STRICT  # Raise a ValueError exception on error.
