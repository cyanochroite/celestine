"""Python Imaging Library (Fork)."""

from celestine.package import (
    Abstract,
    tkinter,
)
from celestine.package.PIL import (
    Image,
    ImageEnhance,
    ImagePalette,
    ImageTk,
)
from celestine.typed import (
    N,
    R,
    ignore,
)

ignore(Image, ImageEnhance, ImagePalette, ImageTk)


class Package(Abstract):
    """"""

    def __init__(self, **star: R) -> N:
        super().__init__(pypi="PIL")
        if self.package and bool(tkinter):
            self.attribute("ImageTk")
