"""Python interface to Tcl/Tk."""

from celestine.package import Abstract
from celestine.typed import (
    A,
    K,
    N,
    R,
    S,
    Z,
)

Button: A
Frame: A
Label: A


class Package(Abstract):
    """"""


class Tk:
    """"""

    def config(self, *, bg: S) -> N:
        """Widthxheight±x±y."""
        raise NotImplementedError(self, bg)

    # pylint: disable-next=invalid-name
    def geometry(self, newGeometry: S) -> N:
        """Widthxheight±x±y."""
        raise NotImplementedError(self, newGeometry)

    def mainloop(self) -> N:
        """"""
        raise NotImplementedError(self)

    def maxsize(self, width: Z, height: Z) -> N:
        """"""
        raise NotImplementedError(self, width, height)

    def minsize(self, width: Z, height: Z) -> N:
        """"""
        raise NotImplementedError(self, width, height)

    def title(self, string: S) -> N:
        """"""
        raise NotImplementedError(self, string)


class PhotoImage:
    """"""

    def height(self) -> K:
        """"""
        raise NotImplementedError(self)

    def subsample(self, x: Z, y: Z) -> K:
        """"""
        raise NotImplementedError(self, x, y)

    def width(self) -> Z:
        """"""
        raise NotImplementedError(self)

    def zoom(self, x: Z, y: Z) -> K:
        """"""
        raise NotImplementedError(self, x, y)

    def __init__(self, **star: R) -> N:
        """"""
        raise NotImplementedError(self, star)
