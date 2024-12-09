""""""

from celestine.package.pygame.abstract import Surface
from celestine.typed import (
    TZ2,
    N,
    S,
)


def flip() -> N:
    """"""
    raise NotImplementedError()


def set_caption(title: S) -> N:
    """"""
    raise NotImplementedError(title)


def set_icon(surface: Surface) -> N:
    """"""
    raise NotImplementedError(surface)


def set_mode(size: TZ2) -> Surface:
    """"""
    raise NotImplementedError(size)
