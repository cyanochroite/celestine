""""""

from celestine.package.pygame.abstract import Surface
from celestine.typed import (
    TZ2,
    N,
    R,
    S,
)


def flip(**star: R) -> N:
    """"""
    raise NotImplementedError()


def set_caption(title: S, **star: R) -> N:
    """"""
    raise NotImplementedError(title)


def set_icon(surface: Surface, **star: R) -> N:
    """"""
    raise NotImplementedError(surface)


def set_mode(size: TZ2, **star: R) -> Surface:
    """"""
    raise NotImplementedError(size)
