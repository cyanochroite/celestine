""""""

from celestine.data import wrapper
from celestine.package.pygame.abstract import Surface
from celestine.typed import (
    TZ2,
    N,
    R,
    S,
)


@wrapper(__name__)
def flip(**star: R) -> N:
    """"""
    raise NotImplementedError()


@wrapper(__name__)
def set_caption(title: S, **star: R) -> N:
    """"""
    raise NotImplementedError(title)


@wrapper(__name__)
def set_icon(surface: Surface, **star: R) -> N:
    """"""
    raise NotImplementedError(surface)


@wrapper(__name__)
def set_mode(size: TZ2, **star: R) -> Surface:
    """"""
    raise NotImplementedError(size)
