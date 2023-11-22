"""Central place for loading and importing external files."""


from celestine.stream.data import (
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


def text(path: P, mode: S) -> FILE:
    """Does all file opperations."""
    encoding = UTF_8  # Use UTF 8 encoding.
    errors = STRICT  # Raise a ValueError exception on error.
    return raw(path, mode, encoding, errors)


class Funny:
    """"""

    def load(self, path: P) -> S:
        """"""
        with self.reader(path) as file:
            return file.read()

    def reader(self, path: P) -> FILE:
        """"""
        return binary(path, READ_BINARY)

    def save(self, path: P, data: S) -> N:
        """"""
        with self.writer(path) as file:
            file.write(data)

    def writer(self, path: P) -> FILE:
        """"""
        return binary(path, WRITE_BINARY)

    def __init__(self) -> N:
        self.encoding = (
            None  # Binary mode doesn't take an 'encoding' argument.
        )
        self.errors = (
            None  #: Binary mode doesn't take an 'errors' argument
        )


class Binary(Funny):
    """"""

    def work(path: P, mode: S) -> FILE:
        """Does all file opperations."""
        encoding = (
            None  # Binary mode doesn't take an 'encoding' argument.
        )
        errors = None  #: Binary mode doesn't take an 'errors' argument
        return raw(path, mode, encoding, errors)

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

    def work(path: P, mode: S) -> FILE:
        """Does all file opperations."""
        encoding = UTF_8  # Use UTF 8 encoding.
        errors = STRICT  # Raise a ValueError exception on error.
        return raw(path, mode, encoding, errors)

    def reader(self, path: P) -> FILE:
        """"""
        return self.work(path, READ_TEXT)

    def writer(self, path: P) -> FILE:
        """"""
        return self.work(path, WRITE_TEXT)

    def __init__(self) -> N:
        encoding = UTF_8  # Use UTF 8 encoding.
        errors = STRICT  # Raise a ValueError exception on error.
        return raw(path, mode, encoding, errors)
