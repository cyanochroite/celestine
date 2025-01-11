"""Python Game Development."""

from celestine.data import (
    Stub,
    stub,
)
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

    @stub(__name__)
    def blit(self, source: K, dest: TZ2) -> Rect:
        """"""
        raise NotImplementedError(self, source, dest)

    @stub(__name__)
    def convert_alpha(self) -> K:
        """"""
        raise NotImplementedError(self)

    @stub(__name__)
    def fill(self, color: TZ3) -> Rect:
        """"""
        raise NotImplementedError(self, color)

    @stub(__name__)
    def get_height(self) -> Z:
        """"""
        raise NotImplementedError(self)

    @stub(__name__)
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
    @stub(__name__)
    def flip(*, call: Stub) -> N:
        """"""
        raise NotImplementedError(call)

    @staticmethod
    @stub(__name__)
    def set_caption(title: S, *, call: Stub) -> N:
        """"""
        raise NotImplementedError(title, call)

    @staticmethod
    @stub(__name__)
    def set_icon(surface: Surface, *, call: Stub) -> N:
        """"""
        raise NotImplementedError(surface, call)

    @staticmethod
    @stub(__name__)
    def set_mode(size: TZ2, *, call: Stub) -> Surface:
        """"""
        raise NotImplementedError(size, call)
