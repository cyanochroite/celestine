"""Python Imaging Library (Fork)."""

import enum

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

    mode: S
    size: TZ2

    class Dither(enum.Enum):
        """"""

        FLOYDSTEINBERG = enum.auto()
        NONE = enum.auto()
        ORDERED = enum.auto()
        RASTERIZE = enum.auto()

    class Palette(enum.Enum):
        """"""

        ADAPTIVE = enum.auto()
        WEB = enum.auto()

    class Resampling(enum.Enum):
        """"""

        BOX = enum.auto()
        BICUBIC = enum.auto()
        BILINEAR = enum.auto()
        HAMMING = enum.auto()
        LANCZOS = enum.auto()
        NEAREST = enum.auto()

    @classmethod
    def open(cls, fp: P, mode: S, formats: N) -> K:
        """"""
        raise NotImplementedError(cls, fp, mode, formats)

    def resize(
        self,
        size: TZ2,
        resample: Resampling,
        box: N,
        reducing_gap: N,
    ) -> K:
        """"""
        raise NotImplementedError(
            self,
            size,
            resample,
            box,
            reducing_gap,
        )

    @property
    def height(self) -> Z:
        result = self.image.height
        return result

    def resize(self, size: TZ2, box) -> N:
        """"""
        # TODO check if box should be set
        size_x, size_y = size

        size_x = max(1, round(size_x))
        size_y = max(1, round(size_y))
        size = (size_x, size_y)

        resample = pillow.Image.Resampling.LANCZOS
        # box = None
        reducing_gap = None

        result = self.image.resize(size, resample, box, reducing_gap)
        self.image = result

    @property
    def size(self) -> TZ2:
        result = self.image.size
        return result

    @property
    def width(self) -> Z:
        result = self.image.width
        return result

    ###

    def convert(self, mode: S, matrix: N, dither: Dither) -> K:
        """"""
        raise NotImplementedError(self, mode, matrix, dither)

    def tobytes(self) -> bytes:
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
        if self.package:
            # TODO: Check for tkinter import as well.
            setattr(self, "ImageTk", load.package("PIL", "ImageTk"))


def extension() -> LS:
    """"""
    raise NotImplementedError()
