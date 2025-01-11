"""Python Game Development."""

from celestine.data import wrapper
from celestine.package import Abstract
from celestine.package.pygame import (
    event,
    font,
    image,
    mouse,
    transform,
)
from celestine.typed import (
    TZ2,
    TZ3,
    K,
    N,
    S,
    W,
    Z,
    ignore,
)

ignore(event)
ignore(font)
ignore(image)
ignore(mouse)
ignore(transform)

MOUSEBUTTONDOWN: Z
QUIT: Z


class Package(Abstract):
    """"""


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

    @wrapper(__name__)
    def blit(self, source: K, dest: TZ2) -> Rect:
        """"""
        raise NotImplementedError(self, source, dest)

    @wrapper(__name__)
    def convert_alpha(self) -> K:
        """"""
        raise NotImplementedError(self)

    @wrapper(__name__)
    def fill(self, color: TZ3) -> Rect:
        """"""
        raise NotImplementedError(self, color)

    @wrapper(__name__)
    def get_height(self) -> Z:
        """"""
        raise NotImplementedError(self)

    @wrapper(__name__)
    def get_width(self) -> Z:
        """"""
        raise NotImplementedError(self)

    def __init__(self, size: TZ2) -> N:
        """"""
        raise NotImplementedError(self, size)


def quit() -> N:  # pylint: disable=redefined-builtin
    """"""


class display:  # pylint: disable=invalid-name
    """"""

    @staticmethod
    @wrapper(__name__)
    def flip(wrap: W = W) -> N:
        """"""
        raise NotImplementedError(wrap)

    @staticmethod
    @wrapper(__name__)
    def set_caption(title: S, wrap: W = W) -> N:
        """"""
        raise NotImplementedError(title, wrap)

    @staticmethod
    @wrapper(__name__)
    def set_icon(surface: Surface, wrap: W = W) -> N:
        """"""
        raise NotImplementedError(surface, wrap)

    @staticmethod
    @wrapper(__name__)
    def set_mode(size: TZ2, wrap: W = W) -> Surface:
        """"""
        raise NotImplementedError(size, wrap)
