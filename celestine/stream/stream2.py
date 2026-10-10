""""""

import os
import pathlib

from celestine import (
    walk,
)
from celestine.stream.data import (
    BINARY,
    COMPRESS,
    DOCUMENT,
)
from celestine.stream.record import (
    Abstract,
    Binary,
    Compress,
    Document,
)
from celestine.typed import (
    B,
    G,
    N,
    P,
    Path,
    S,
    ignore,
)


class Carrot:
    """"""

    root: P

    def binary(self, *paths: Path) -> Binary:
        """"""
        path = self.path(*paths)
        result = Binary(path)
        return result

    def compress(self, *paths: Path) -> Compress:
        """"""
        path = self.path(*paths)
        result = Compress(path)
        return result

    def document(self, *paths: Path) -> Document:
        """"""
        path = self.path(*paths)
        result = Document(path)
        return result

    def path(self, *paths: Path) -> P:
        """"""
        make: S = os.path.join(self.root, *paths)
        norm: S = os.path.normpath(make)
        real: S = os.path.realpath(norm, strict=False)

        safe = os.path.commonpath((self.root, real))

        if not os.path.samefile(self.root, safe):
            raise RuntimeError()

        result = pathlib.Path(real)
        return result

    def records(self) -> G[Abstract]:
        """"""
        for record in walk.record(self.root, [], []):
            path: P = record
            suffix = path.suffix

            if suffix in BINARY:
                yield Binary(path)
                continue

            if suffix in COMPRESS:
                yield Compress(path)
                continue

            if suffix in DOCUMENT:
                yield Document(path)
                continue

            raise ValueError()

    def __init__(self, *paths: Path) -> N:
        self.root = pathlib.Path(*paths)


ignore(
    Carrot,
)
