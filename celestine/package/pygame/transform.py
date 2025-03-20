""""""

from celestine.data import wrapper
from celestine.package.pygame.abstract import Surface
from celestine.typed import (
    TZ2,
    R,
)


@wrapper(__name__)
def smoothscale(surface: Surface, size: TZ2, **star: R) -> Surface:
    """"""
    raise NotImplementedError(surface, size)
