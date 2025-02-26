"""Python interface to Tcl/Tk."""

from celestine.package import Abstract
from celestine.typed import (
    TD,
    K,
    N,
    R,
    S,
    U,
    Z,
)


class Package(Abstract):
    """"""


class PhotoImage:
    """"""

    def height(self) -> Z:
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


class _Configure(TD):
    """"""

    image: PhotoImage
    text: S


class _Frame(TD):
    """"""

    bg: S
    height: Z
    padx: Z
    pady: Z
    width: Z


class Button:
    """"""

    def configure(self, **star: U[_Configure]) -> N:
        """"""
        raise NotImplementedError(self, star)

    def place_forget(self) -> N:
        """"""
        raise NotImplementedError(self)

    def __init__(self, window: K) -> N:
        raise NotImplementedError(self, window)


class Frame:
    """"""

    def __init__(self, window: K, **star: U[_Frame]) -> N:
        raise NotImplementedError(self, window, star)


class Label:
    """"""

    def configure(self, **star: U[_Configure]) -> N:
        """"""
        raise NotImplementedError(self)

    def place_forget(self) -> N:
        """"""
        raise NotImplementedError(self)

    def __init__(self, window: K) -> N:
        raise NotImplementedError(self, window)
