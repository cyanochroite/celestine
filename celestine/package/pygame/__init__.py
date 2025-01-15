"""Python Game Development."""

from celestine.data import wrapper
from celestine.package import Abstract
from celestine.package.pygame import (
    display,
    event,
    font,
    image,
    mouse,
    transform,
)
from celestine.package.pygame.abstract import Surface
from celestine.typed import (
    LS,
    N,
    R,
    Z,
    ignore,
    override,
)

ignore(Surface)
ignore(display)
ignore(event)
ignore(font)
ignore(image)
ignore(mouse)
ignore(transform)


MOUSEBUTTONDOWN: Z
QUIT: Z


class Package(Abstract):
    """"""

    @override
    def exempt(self) -> LS:
        """"""
        ignore(self)
        return ["MOUSEBUTTONDOWN", "QUIT"]


class Rect:
    """"""


@wrapper(__name__)
def quit(**star: R) -> N:  # pylint: disable=redefined-builtin
    """"""
    raise NotImplementedError()
