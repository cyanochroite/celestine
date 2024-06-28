"""Python Game Development."""

from celestine.package import Abstract
from celestine.typed import (
    A,
    M,
    T,
    Z,
    ignore,
)

MOUSEBUTTONDOWN: A
QUIT: A
canvas: A
display: A
event: A
font: A
image: A
mouse: A
quit: A  # pylint: disable=redefined-builtin


class Surface:
    """"""


class Transform:
    """"""

    def smoothscale(self, surface: Surface, size: T[Z, Z]) -> Surface:
        """"""
        ignore(surface)
        ignore(size)
        return Surface()


transform = Transform()


class Package(Abstract):
    """"""

    image: M
