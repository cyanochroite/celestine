"""Central place for loading and importing external files."""

import lzma

from celestine.file import (
    READ_BINARY,
    WRITE_BINARY,
)
from celestine.typed import (
    LZMA,
    N,
    P,
    S,
)


def lzma_load(path: P) -> LZMA:
    """"""
    return lzma.open(
        path,
        mode=READ_BINARY,
    )


def lzma_read(path: P) -> S:
    """"""
    with lzma_load(path) as file:
        return file.read()


def lzma_save(path: P) -> LZMA:
    """"""
    return lzma.open(
        path,
        mode=WRITE_BINARY,
        format=lzma.FORMAT_XZ,
        check=lzma.CHECK_SHA256,
        preset=9,
        filters=None,
    )


def lzma_write(path: P, data: S) -> N:
    """"""
    with lzma_save(path) as file:
        file.write(bytes(data))
