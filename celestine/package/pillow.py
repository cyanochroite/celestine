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
    Z,
)


class Image:
    """"""

    class Dither:
        """"""

        FLOYDSTEINBERG = 0
        NONE = 0
        ORDERED = 0
        RASTERIZE = 0

    class Palette:
        """"""

        ADAPTIVE = 0
        WEB = 0

    class Resampling:
        """"""

        BICUBIC = 0
        BILINEAR = 0
        BOX = 0
        HAMMING = 0
        LANCZOS = 0
        NEAREST = 0

    @property
    def height(self) -> Z: ...

    @classmethod
    def open(cls, fp: P, mode: S, formats: N) -> K: ...

    def resize(
        self,
        size: TZ2,
        resample: Resampling,
        box: N,
        reducing_gap: N,
    ) -> K: ...

    @property
    def size(self) -> TZ2: ...

    @property
    def width(self) -> Z: ...

    ###
    def convert(self, mode: S, matrix: N, dither: Dither) -> K: ...

    def tobytes(self) -> bytes: ...


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
