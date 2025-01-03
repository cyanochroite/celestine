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

    @classmethod
    def open(cls, fp: P, mode: S, formats: N) -> K:
        """"""
        raise NotImplementedError(cls, fp, mode, formats)

    class Dither(enum.Enum):
        """"""

        FLOYDSTEINBERG = enum.auto()

    class Palette(enum.Enum):
        """"""

        WEB = enum.auto()

    class Resampling(enum.Enum):
        """"""

        LANCZOS = enum.auto()

    def convert(self, mode: S, matrix: N, dither: Dither) -> K:
        """"""
        raise NotImplementedError(self, mode, matrix, dither)

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
