""""""

from celestine import bank
from celestine.data import (
    wrap,
    wrapper,
)
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


@wrapper(__name__)
class Image:
    """"""

    mode: S

    @wrapper(__name__)
    def convert(self, mode: S, matrix: N, dither: "Dither") -> K:
        """"""
        raise NotImplementedError(self, mode, matrix, dither)

    @wrapper(__name__)
    def getdata(self, im: K, box: TZ4) -> L[Z] | L[TZ3]:
        """"""
        raise NotImplementedError(self, im, box)

    @property
    @wrapper(__name__)
    def height(self) -> Z:
        """"""
        raise NotImplementedError(self)

    @wrapper(__name__)
    def paste(self, im: K, box: TZ4) -> K:
        """"""
        raise NotImplementedError(self, im, box)

    @wrapper(__name__)
    def putpalette(self, data: LZ, rawmode: S) -> N:
        """"""
        raise NotImplementedError(self, data, rawmode)

    @wrapper(__name__)
    def quantize(self, *, palette, **star: R) -> Y:
        """"""
        ignore(self)
        # TODO local class not being called
        result = wrap(colors=255, palette=palette, **star)
        return result

    @wrapper(__name__)
    def resize(self, size: TZ2, resample: Resampling) -> K:
        """"""
        raise NotImplementedError(self, size, resample)

    @property
    @wrapper(__name__)
    def size(self) -> TZ2:
        """"""
        raise NotImplementedError(self)

    @wrapper(__name__)
    def tobytes(self) -> Y:
        """"""
        raise NotImplementedError(self)

    @property
    @wrapper(__name__)
    def width(self) -> Z:
        """"""
        raise NotImplementedError(self)


@wrapper(__name__)
def new(mode: S, size: TZ2, **star: R) -> Image:
    """"""
    color = 0
    result = wrap(mode, size, color, **star)
    return result


@wrapper(__name__)
# pylint: disable-next=redefined-builtin
def open(path: P, **star: R) -> Image:
    """"""
    fp = path
    mode = LATIN_SMALL_LETTER_R
    formats = bank.window.formats()
    result = wrap(fp, mode, formats, **star)
    return result


@wrapper(__name__)
def registered_extensions() -> LS:
    """"""
    raise NotImplementedError()
