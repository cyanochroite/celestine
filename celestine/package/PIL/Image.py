""""""

from celestine import bank
from celestine.data import wrap
from celestine.literal import LATIN_SMALL_LETTER_R
from celestine.typed import (
    LS,
    LZ,
    TZ2,
    TZ3,
    TZ4,
    K,
    L,
    N,
    P,
    R,
    S,
    Y,
    Z,
    ignore,
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

    def getdata(self, im: K, box: TZ4) -> L[Z] | L[TZ3]:
        """"""
        raise NotImplementedError(self, im, box)

    @property
    def height(self) -> Z:
        """"""
        raise NotImplementedError(self)

    def paste(self, im: K, box: TZ4) -> K:
        """"""
        raise NotImplementedError(self, im, box)

    def putpalette(self, data: LZ, rawmode: S) -> N:
        """"""
        raise NotImplementedError(self, data, rawmode)

    def quantize(self, *, palette, **star: R) -> Y:
        """"""
        ignore(self)
        # TODO local class not being called
        result = wrap(colors=255, palette=palette, **star)
        return result

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


def new(mode: S, size: TZ2, **star: R) -> Image:
    """"""
    color = 0
    result = wrap(mode, size, color, **star)
    return result


# pylint: disable-next=redefined-builtin
def open(path: P, **star: R) -> Image:
    """"""
    fp = path
    mode = LATIN_SMALL_LETTER_R
    formats = bank.window.formats()
    result = wrap(fp, mode, formats, **star)
    return result


def registered_extensions() -> LS:
    """"""
    raise NotImplementedError()
