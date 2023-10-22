"""Central place for loading and importing external files."""

import lzma

from celestine.file import data as stream
from celestine.typed import (
    N,
    P,
    S,
)

type LZMA = lzma.LZMAFile


def load(filename: P) -> LZMA:
    """"""
    return lzma.open(
        filename,
        mode=stream.READ_BINARY,
    )


def save(filename: P) -> LZMA:
    """"""
    return lzma.open(
        filename,
        mode=stream.WRITE_BINARY,
        format=lzma.FORMAT_XZ,
        check=lzma.CHECK_SHA256,
        preset=9,
        filters=None,
    )


def load_data(filename: P) -> S:
    """"""
    with load(filename) as file:
        return file.read()


def save_data(filename: P, data: S) -> N:
    """"""
    with save(filename) as file:
        file.write(bytes(data))
