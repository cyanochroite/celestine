""""""

from celestine.typed import (
    TZ2,
    TZ3,
    K,
    N,
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

    def blit(self, source: K, dest: TZ2) -> Rect:
        """"""
        raise NotImplementedError(self, source, dest)

    def convert_alpha(self) -> K:
        """"""
        raise NotImplementedError(self)

    def fill(self, color: TZ3) -> Rect:
        """"""
        raise NotImplementedError(self, color)

    def get_height(self) -> Z:
        """"""
        raise NotImplementedError(self)

    def get_width(self) -> Z:
        """"""
        raise NotImplementedError(self)
