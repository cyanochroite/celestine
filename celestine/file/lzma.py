"""Central place for loading and importing external files."""

import lzma

from celestine.typed import (
    LZMA,
    N,
    P,
    S,
)
from . import data as stream


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
    data = None
    with load(filename) as file:
        data = file.read()
    return data


def save_data(filename: P, data: S) -> N:
    """"""
    with save(filename) as file:
        file.write(bytes(data))

