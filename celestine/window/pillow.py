"""Python Imaging Library (Fork)."""

from celestine.literal import LATIN_SMALL_LETTER_R
from celestine.package import pillow
from celestine.typed import (
    TZ2,
    K,
    N,
    P,
)


class Image:
    """"""
    image: pillow.Image

    def resize(self, size: TZ2) -> N:
        """"""
        # TODO check if box should be set
        size_x, size_y = size

        size_x = max(1, round(size_x))
        size_y = max(1, round(size_y))
        size = (size_x, size_y)

        resample = pillow.Image.Resampling.LANCZOS
        box = None
        reducing_gap = None

        result = self.image.resize(size, resample, box, reducing_gap)
        self.image = result

    ###

    def convert(self) -> N:
        """"""
        mode = "RGBA"
        matrix = None
        dither = pillow.Image.Dither.NONE
        palette = pillow.Image.Palette.ADAPTIVE
        colors = 256
        hold = self.image.convert(mode, matrix, dither, palette, colors)
        self.image = hold

    @classmethod
    def open(cls, path: P) -> K:
        """"""
        fp = path
        mode = LATIN_SMALL_LETTER_R
        formats = None
        image = pillow.Image.open(fp, mode, formats)
        result = cls(image)
        return result

    def __init__(self, image: pillow.Image) -> N:
        self.image = image
