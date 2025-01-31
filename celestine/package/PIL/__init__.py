"""Python Imaging Library (Fork)."""

from celestine import load
from celestine.package import (
    Abstract,
    tkinter,
)
from celestine.package.PIL import (
    Image,
    ImageTk,
)
from celestine.typed import (
    N,
    R,
    ignore,
)

ignore(Image)
ignore(ImageTk)


class Package(Abstract):
    """"""

    def __init__(self, **star: R) -> N:
        super().__init__(pypi="PIL")
        setattr(self, "ImageEnhance", load.package("PIL", "ImageEnhance"))

        if self.package and bool(tkinter):
            setattr(self, "ImageTk", load.package("PIL", "ImageTk"))
