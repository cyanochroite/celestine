"""Python Imaging Library (Fork)."""

from celestine import load
from celestine.package import (
    Abstract,
    tkinter,
)
from celestine.package.pillow import Image
from celestine.typed import (
    LS,
    VP,
    N,
    R,
    Z,
    ignore,
)

ignore(Image)


class ImageTk:
    """"""

    class PhotoImage:
        """"""

        def height(self) -> Z:
            """"""
            raise NotImplementedError(self)

        def width(self) -> Z:
            """"""
            raise NotImplementedError(self)

        def __init__(self, image: VP = None) -> N:
            """"""
            raise NotImplementedError(self, image)


class Package(Abstract):
    """"""

    def __init__(self, **star: R) -> N:
        super().__init__(pypi="PIL")
        if self.package and bool(tkinter):
            setattr(self, "ImageTk", load.package("PIL", "ImageTk"))


def extension() -> LS:
    """"""
    raise NotImplementedError()
