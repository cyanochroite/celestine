""""""

from celestine.package.pygame.abstract import Surface
from celestine.typed import (
    TZ2,
    P,
    S,
    Y,
)


def frombuffer(buffer: Y, size: TZ2, format_: S) -> Surface:
    """"""
    raise NotImplementedError(buffer, size, format_)


def load(filename: P) -> Surface:
    """"""
    raise NotImplementedError(filename)
