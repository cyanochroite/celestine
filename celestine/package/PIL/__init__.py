"""Python Imaging Library (Fork)."""

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
        self.attribute("ImageEnhance")
        if self.package and bool(tkinter):
            self.attribute("ImageTk")
