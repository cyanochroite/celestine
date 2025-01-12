""""""

from celestine import bank
from celestine.data import wrapper
from celestine.literal import LATIN_SMALL_LETTER_R
from celestine.typed import (
    TZ2,
    K,
    N,
    P,
    R,
    S,
    Y,
    Z,
)


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


class Image:
    """"""

    mode: S

    def convert(self, mode: S, matrix: N, dither: "Dither") -> K:
        """"""
        raise NotImplementedError(self, mode, matrix, dither)

    @property
    def height(self) -> Z:
        """"""
        raise NotImplementedError(self)

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


@wrapper(__name__)
# pylint: disable-next=redefined-builtin
def open(path: P, **star: R) -> Image:
    """"""
    wrap = star.get("warp")
    if not wrap:
        raise NotImplementedError(path)

    fp = path
    mode = LATIN_SMALL_LETTER_R
    formats = bank.window.formats()
    result = wrap(fp, mode, formats)
    return result
