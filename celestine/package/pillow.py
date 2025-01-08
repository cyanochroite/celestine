"""Python Imaging Library (Fork)."""

from celestine import load
from celestine.package import Abstract
from celestine.typed import (
    LS,
    TZ2,
    VP,
    K,
    N,
    P,
    R,
    S,
    Y,
    Z,
)


class Image:
    """"""

    class Dither:
        """"""

        FLOYDSTEINBERG = 1
        NONE = 2
        ORDERED = 3
        RASTERIZE = 4

    class Palette:
        """"""

        ADAPTIVE = 1
        WEB = 2

    class Resampling:
        """"""

        BICUBIC = 1
        BILINEAR = 2
        BOX = 3
        HAMMING = 4
        LANCZOS = 5
        NEAREST = 6

    def convert(self, mode: S, matrix: N, dither: Dither) -> K: ...

    @property
    def height(self) -> Z: ...

    @classmethod
    def open(cls, fp: P, mode: S, formats: LS) -> K: ...

    def resize(self, size: TZ2, resample: Resampling) -> K: ...

    @property
    def size(self) -> TZ2: ...

    def tobytes(self) -> Y: ...

    @property
    def width(self) -> Z: ...


class ImageTk:
    """"""

    class PhotoImage:
        """"""

        def height(self) -> Z: ...
        def width(self) -> Z: ...
        def __init__(self, image: VP = None) -> N: ...


class Package(Abstract):
    """"""

    def __init__(self, **star: R) -> N:
        super().__init__(pypi="PIL")
        if self.package:
            # TODO: Check for tkinter import as well.
            setattr(self, "ImageTk", load.package("PIL", "ImageTk"))


def extension() -> LS: ...
