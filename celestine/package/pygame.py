"""Python Game Development."""

from celestine.package import Abstract
from celestine.typed import (
    A,
    M,
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


class Package(Abstract):
    """"""

    image: M
