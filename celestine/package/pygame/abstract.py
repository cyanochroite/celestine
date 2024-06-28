""""""

from celestine.typed import (
    TZ2,
    TZ3,
    K,
    N,
    Z,
    ignore,
)


class Event:
    """"""

    type: Z
    button: Z


class Font:
    """"""


class Rect:
    """"""


class Surface:
    """"""

    def blit(self, source: K, dest: TZ2) -> Rect:
        """"""
        ignore(source)
        ignore(dest)
        return Rect()

    @staticmethod
    def convert_alpha() -> K:
        """"""
        return K

    def fill(self, color: TZ3) -> Rect:
        """"""
        ignore(color)
        return Rect()

    def get_height(self) -> Z:
        """"""
        return 0

    def get_width(self) -> Z:
        """"""
        return 0

    def __init__(self, size: TZ2) -> N:
        """"""
        ignore(size)


EVENT = Event()
SURFACE = Surface((0, 0))
SIZE = (0, 0)
