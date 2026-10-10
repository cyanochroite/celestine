""""""

from celestine.package.pygame.abstract import Surface
from celestine.typed import (
    TZ2,
    N,
    R,
    S,
    ignore,
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


ignore(flip, set_caption, set_icon, set_mode)
