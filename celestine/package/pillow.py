"""Python Imaging Library (Fork)."""

import enum
import typing

from celestine import load
from celestine.package import Abstract
from celestine.typed import (
    TZ2,
    K,
    N,
    P,
    R,
    S,
)


class Image(typing.Protocol):
    """"""

    mode: S
    size: TZ2

    @classmethod
    def open(cls, fp: P) -> K:
        """"""
        raise NotImplementedError(cls, fp)

    class Resampling(enum.Enum):
        """"""

        LANCZOS = enum.auto()

    def resize(self, size: TZ2, resample: Resampling) -> K:
        """"""
        raise NotImplementedError(self, size, resample)

    def tobytes(self) -> bytes:
        """"""
        raise NotImplementedError(self)


class Package(Abstract):
    """"""

    def __init__(self, **star: R) -> N:
        super().__init__(pypi="PIL")
        if self.package:
            # TODO: Check for tkinter import as well.
            setattr(self, "ImageTk", load.package("PIL", "ImageTk"))
