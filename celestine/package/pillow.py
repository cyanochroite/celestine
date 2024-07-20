"""Python Imaging Library (Fork)."""

import enum

from celestine import load
from celestine.package import Abstract
from celestine.typed import (
    TZ2,
    K,
    N,
    P,
    R,
    S,
    ignore,
)


class Image:
    """"""

    mode: S
    size: TZ2

    @staticmethod
    def open(fp: P) -> K:
        """"""
        ignore(fp)
        return Image()

    class Resampling(enum.Enum):
        """"""

        LANCZOS = enum.auto()

    def resize(self, size: TZ2, resample: Resampling) -> K:
        """"""
        ignore(size)
        ignore(resample)
        return Image()

    def tobytes(self) -> bytes:
        """"""
        return b""

    def __init__(self):
        self.size = (0, 0)


class Package(Abstract):
    """"""

    def __init__(self, **star: R) -> N:
        super().__init__(pypi="PIL")
        if self.package:
            # TODO: Check for tkinter import as well.
            setattr(self, "ImageTk", load.package("PIL", "ImageTk"))
