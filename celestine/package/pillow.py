"""Python Imaging Library (Fork)."""

from celestine.data import stub
from celestine import load, bank
from celestine.package import (
    Abstract,
    tkinter,
)
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
    ignore,
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

    def convert(self, mode: S, matrix: N, dither: Dither) -> K:
        """"""
        raise NotImplementedError(self, mode, matrix, dither)

    @property
    def height(self) -> Z:
        """"""
        raise NotImplementedError(self)

    @staticmethod
    @stub(__name__)
    def open(fp: P, mode: S, formats: LS) -> K:
        """"""
        package = bank.package["pillow"].package
        return package.Image.open(fp, mode, formats)

    def resize(self, size: TZ2, resample: Resampling) -> K:
        """"""
        raise NotImplementedError(self, size, resample)

    @property
    def size(self) -> TZ2:
        """"""
        raise NotImplementedError(self)

    def tobytes(self) -> Y:
        """"""
        raise NotImplementedError(self)

    @property
    def width(self) -> Z:
        """"""
        raise NotImplementedError(self)


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
