"""Python Imaging Library (Fork)."""

from celestine.literal import LATIN_SMALL_LETTER_R
from celestine.package import pillow
from celestine.typed import (
    LS,
    TZ2,
    A,
    K,
    N,
    P,
    Z,
)


class Image:
    """"""

    image: pillow.Image

    @property
    def height(self) -> Z:
        """"""
        result = self.image.height
        return result

    def resize(self, sizes: TZ2, box: A) -> N:
        """"""
        size_x, size_y = sizes

        size_x = max(1, round(size_x))
        size_y = max(1, round(size_y))

        size = (size_x, size_y)
        resample = pillow.Image.Resampling.LANCZOS

        result = self.image.resize(size, resample)
        self.image = result

    @property
    def size(self) -> TZ2:
        """"""
        result = self.image.size
        return result

    @property
    def width(self) -> Z:
        """"""
        result = self.image.width
        return result

    ###

    def convert(self) -> N:
        """"""
        mode = "RGBA"
        matrix = None
        dither = pillow.Image.Dither.NONE  # TODO: Erase?
        hold = self.image.convert(mode, matrix, dither)
        self.image = hold

    @classmethod
    def open(cls, path: P, format: LS) -> K:
        """"""
        fp = path
        mode = LATIN_SMALL_LETTER_R
        formats = format
        image = pillow.Image.open(fp, mode, formats)
        result = cls(image)
        return result

    def __init__(self, image: pillow.Image) -> N:
        self.image = image
