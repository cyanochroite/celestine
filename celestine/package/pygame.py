"""Python Game Development."""

from celestine.package import Abstract
from celestine.typed import (
    TZ2,
    TZ3,
    K,
    N,
    S,
    P,
    Z,
    ignore,
)


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

    def fill(self, color: TZ3) -> Rect:
        """"""
        ignore(color)
        return Rect()

    def __init__(self, size: TZ2) -> N:
        """"""
        ignore(size)


########################################################################
SIZE = (0, 0)
SURFACE = Surface(SIZE)
########################################################################


class display:  # pylint: disable=invalid-name
    """"""

    @staticmethod
    def flip() -> N:
        """"""

    @staticmethod
    def set_caption(title: S) -> N:
        """"""
        ignore(title)

    @staticmethod
    def set_icon(surface: Surface) -> N:
        """"""
        ignore(surface)

    @staticmethod
    def set_mode(size: TZ2) -> Surface:
        """"""
        ignore(size)
        return Surface(SIZE)


class event:  # pylint: disable=invalid-name
    """"""

    @staticmethod
    def wait() -> N:
        """"""


class font:  # pylint: disable=invalid-name
    """"""

    @staticmethod
    def init() -> N:
        """"""

    @staticmethod
    def Font(file_path: P, size: Z) -> Font:
        """"""
        ignore(file_path)
        ignore(size)
        return Font()


class image:  # pylint: disable=invalid-name
    """"""

    @staticmethod
    def frombuffer(buffer, size, format_) -> Surface:
        """"""
        ignore(buffer)
        ignore(size)
        ignore(format_)
        return SURFACE

    @staticmethod
    def load(filename: P) -> Surface:
        """"""
        ignore(filename)
        return SURFACE


class mouse:  # pylint: disable=invalid-name
    """"""

    @staticmethod
    def get_pos() -> TZ2:
        """"""
        return SIZE


def quit() -> N:  # pylint: disable=redefined-builtin
    """"""


class transform:  # pylint: disable=invalid-name
    """"""

    @staticmethod
    def smoothscale(surface: Surface, size: TZ2) -> Surface:
        """"""
        ignore(surface)
        ignore(size)
        return SURFACE
########################################################################


class Package(Abstract):
    """"""
