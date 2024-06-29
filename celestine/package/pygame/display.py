""""""

from celestine.package.pygame.abstract import (
    SURFACE,
    Surface,
)
from celestine.typed import (
    TZ2,
    N,
    S,
    ignore,
)


def flip() -> N:
    """"""


def set_caption(title: S) -> N:
    """"""
    ignore(title)


def set_icon(surface: Surface) -> N:
    """"""
    ignore(surface)


def set_mode(size: TZ2) -> Surface:
    """"""
    ignore(size)
    return SURFACE
