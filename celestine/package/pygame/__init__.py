"""Python Game Development."""

from celestine.package import Package
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
    R,
    Z,
    ignore,
)

ignore(Surface, display, event, font, image, mouse, transform)


MOUSEBUTTONDOWN: Z
QUIT: Z



class Rect:
    """"""

class Self(Package):
    """"""



def quit(**star: R) -> N:  # pylint: disable=redefined-builtin
    """"""
    raise NotImplementedError()
