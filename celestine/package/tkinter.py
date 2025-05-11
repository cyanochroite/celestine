"""Python interface to Tcl/Tk."""

from celestine.package import Package
from celestine.typed import (
    NR,
    TD,
    UN,
    K,
    N,
    P,
    S,
    U,
    Z,
    ignore,
)


class _TypedConfigure(TD):
    """"""

    bg: S
    image: NR["PhotoImage"]
    text: NR[S]


class _TypedFrame(TD):
    """"""

    bg: S
    height: Z
    padx: Z
    pady: Z
    width: Z


class _TypedPhoto(TD):
    """"""

    file: NR[P]
    height: NR[Z]
    width: NR[Z]


type _Window = U["Frame", "Tk"]


class Button:
    """"""

    def configure(self, **star: UN[_TypedConfigure]) -> N:
        """"""
        raise NotImplementedError(self, star)

    def place_forget(self) -> N:
        """"""
        raise NotImplementedError(self)

    def __init__(self, window: _Window) -> N:
        raise NotImplementedError(self, window)


class Frame:
    """"""

    def __init__(self, window: _Window, **star: UN[_TypedFrame]) -> N:
        raise NotImplementedError(self, window, star)


class Label:
    """"""

    def configure(self, **star: UN[_TypedConfigure]) -> N:
        """"""
        raise NotImplementedError(self, star)

    def place_forget(self) -> N:
        """"""
        raise NotImplementedError(self)

    def __init__(self, window: _Window) -> N:
        raise NotImplementedError(self, window)


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

    def __init__(self, **star: UN[_TypedPhoto]) -> N:
        """"""
        raise NotImplementedError(self, star)


class Self(Package):
    """"""


class Tk:
    """"""

    def configure(self, **star: UN[_TypedConfigure]) -> N:
        """Widthxheight±x±y."""
        raise NotImplementedError(self, star)

    def geometry(self, new_geometry: S, /) -> N:
        """Widthxheight±x±y."""
        raise NotImplementedError(self, new_geometry)

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


ignore(Button, Frame, Label, Package, Tk)
