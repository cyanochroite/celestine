"""Python Imaging Library (Fork)."""

from celestine.package import (
    Package,
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


class Self(Package):
    """"""

    def __init__(self, **star: R) -> N:
        super().__init__(pypi="PIL")
        self.attribute("ImageEnhance")
        if bool(tkinter):
            self.attribute("ImageTk")
