"""Python interface to Tcl/Tk."""

from celestine.data import wrapper
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


@wrapper(__name__)
class Tk:
    """"""

    @wrapper(__name__)
    def config(self, *, bg: S) -> N:
        """Widthxheight±x±y."""
        raise NotImplementedError(self, bg)

    @wrapper(__name__)
    # pylint: disable-next=invalid-name
    def geometry(self, newGeometry: S) -> N:
        """Widthxheight±x±y."""
        raise NotImplementedError(self, newGeometry)

    @wrapper(__name__)
    def mainloop(self) -> N:
        """"""
        raise NotImplementedError(self)

    @wrapper(__name__)
    def maxsize(self, width: Z, height: Z) -> N:
        """"""
        raise NotImplementedError(self, width, height)

    @wrapper(__name__)
    def minsize(self, width: Z, height: Z) -> N:
        """"""
        raise NotImplementedError(self, width, height)

    @wrapper(__name__)
    def title(self, string: S) -> N:
        """"""
        raise NotImplementedError(self, string)


@wrapper(__name__)
class PhotoImage:
    """"""

    # TODO check names.

    @wrapper(__name__)
    def height(self) -> K:
        """"""
        raise NotImplementedError(self)

    @wrapper(__name__)
    def subsample(self, x: Z, y: Z) -> K:
        """"""
        raise NotImplementedError(self, x, y)

    @wrapper(__name__)
    def width(self) -> Z:
        """"""
        raise NotImplementedError(self)

    @wrapper(__name__)
    def zoom(self, x: Z, y: Z) -> K:
        """"""
        raise NotImplementedError(self, x, y)

    def __init__(self, **star: R) -> N:
        """"""
        raise NotImplementedError(self, star)
