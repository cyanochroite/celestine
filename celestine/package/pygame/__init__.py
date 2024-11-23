"""Python Game Development."""

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
    N,
    Z,
    ignore,
)

ignore(display)
ignore(event)
ignore(font)
ignore(image)
ignore(mouse)
ignore(Surface)
ignore(transform)
MOUSEBUTTONDOWN: Z
QUIT: Z


class Package(Abstract):
    """"""


def quit() -> N:  # pylint: disable=redefined-builtin
    """"""
