"""Python interface to Tcl/Tk."""

from celestine.data import wrapper
from celestine.package import Abstract
from celestine.typed import (
    A,
    N,
    S,
    Z,
)

Button: A
Frame: A
Label: A
PhotoImage: A


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
