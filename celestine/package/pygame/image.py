""""""

from celestine.package.pygame.abstract import Surface
from celestine.typed import (
    TZ2,
    P,
    R,
    S,
    Y,
)


def frombuffer(buffer: Y, size: TZ2, format_: S, **star: R) -> Surface:
    """"""
    raise NotImplementedError(buffer, size, format_)


def load(filename: P, **star: R) -> Surface:
    """"""
    raise NotImplementedError(filename)
