""""""

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


class Surface:
    """"""

    color: TZ3
    dest: TZ2
    height: Z
    size: TZ2
    source: K
    width: Z

    def blit(self, source: K, dest: TZ2, **star: R) -> Rect:
        """"""
        raise NotImplementedError(self, source, dest)

    def convert_alpha(self, **star: R) -> K:
        """"""
        raise NotImplementedError(self)

    def fill(self, color: TZ3, **star: R) -> Rect:
        """"""
        raise NotImplementedError(self, color)

    def get_height(self, **star: R) -> Z:
        """"""
        raise NotImplementedError(self)

    def get_width(self, **star: R) -> Z:
        """"""
        raise NotImplementedError(self)

    def __init__(self, size: TZ2, **star: R) -> N:
        """"""
        raise NotImplementedError(self, size)
