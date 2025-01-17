""""""

from celestine.data import wrapper
from celestine.typed import (
    TZ2,
    TZ3,
    K,
    N,
    R,
    Z,
)


class Rect:
    """"""


@wrapper(__name__)
class Surface:
    """"""

    color: TZ3
    dest: TZ2
    height: Z
    size: TZ2
    source: K
    width: Z

    @wrapper(__name__)
    def blit(self, source: K, dest: TZ2, **star: R) -> Rect:
        """"""
        raise NotImplementedError(self, source, dest)

    @wrapper(__name__)
    def convert_alpha(self, **star: R) -> K:
        """"""
        raise NotImplementedError(self)

    @wrapper(__name__)
    def fill(self, color: TZ3, **star: R) -> Rect:
        """"""
        raise NotImplementedError(self, color)

    @wrapper(__name__)
    def get_height(self, **star: R) -> Z:
        """"""
        raise NotImplementedError(self)

    @wrapper(__name__)
    def get_width(self, **star: R) -> Z:
        """"""
        raise NotImplementedError(self)

    def __init__(self, size: TZ2) -> N:
        """"""
        raise NotImplementedError(self, size)
