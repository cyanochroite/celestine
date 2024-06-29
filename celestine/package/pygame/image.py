""""""

from celestine.package.pygame.abstract import (
    SURFACE,
    Surface,
)
from celestine.typed import (
    TZ2,
    P,
    S,
    ignore,
)


def frombuffer(buffer: bytes, size: TZ2, format_: S) -> Surface:
    """"""
    ignore(buffer)
    ignore(size)
    ignore(format_)
    return SURFACE


def load(filename: P) -> Surface:
    """"""
    ignore(filename)
    return SURFACE
