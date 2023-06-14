""""""

from celestine import load
from celestine.typed import (
    L,
    S,
)

from . import Abstract

########################################################################

COLORS = 15  # int(255 - 8 / 16)


class Image:
    def brightwing(self):
        """
        Brightwing no like the dark colors.

        Make image bright.
        """
        pillow = self.ring.package.pillow

        def brighter(pixel):
            invert = (255 - pixel) / 255
            boost = invert * 64
            shift = pixel + boost
            return shift

        hue, saturation, value = self.image.convert("HSV").split()
        new_value = value.point(brighter)

        bands = (hue, saturation, new_value)

        self.image = pillow.Image.merge("HSV", bands).convert("RGB")

    def convert(self, mode):
        """"""
        pillow = self.ring.package.pillow

        matrix = None  # Unused default.
        dither = pillow.Image.Dither.FLOYDSTEINBERG
        palette = pillow.Image.Palette.WEB  # Unused default.
        colors = 256  # Unused default.

        hold = self.image.convert(mode, matrix, dither, palette, colors)
        self.image = hold

    def convert_to_color(self):
        """"""
        self.convert("RGB")

    def convert_to_mono(self):
        """"""

        self.convert("1")

    def getdata(self):
        return self.image.getdata()

    def resize(self, size_x, size_y, box=None):
        """"""
        pillow = self.ring.package.pillow

        size_x = max(1, round(size_x))
        size_y = max(1, round(size_y))

        size = (size_x, size_y)
        resample = pillow.Image.Resampling.LANCZOS
        reducing_gap = None

        hold = self.image.resize(size, resample, box, reducing_gap)
        self.image = hold

    @property
    def size(self):
        """"""
        return self.image.size

    def quantize(self):
        """"""
        pillow = self.ring.package.pillow

        colors = COLORS
        method = pillow.Image.Quantize.MEDIANCUT
        kmeans = 0
        palette = None
        dither = pillow.Image.Dither.FLOYDSTEINBERG

        self.image = self.image.quantize(
            colors, method, kmeans, palette, dither
        )

    def __init__(self, ring, /, image, **star):
        self.ring = ring
        self.image = image


class Package(Abstract):
    """"""

    def image_clone(self, item):
        """"""
        image = item.image.copy()
        new = Image(self.ring, image)
        return new

    def image_load(self, path):
        """"""
        pillow = self.ring.package.pillow

        mode = "r"
        formats = None
        image = pillow.Image.open(path, mode, formats)

        # Highest mode for median cut.
        mode = "RGB"
        matrix = None
        dither = pillow.Image.Dither.NONE
        palette = pillow.Image.Palette.ADAPTIVE
        colors = 256
        image = image.convert(mode, matrix, dither, palette, colors)

        new = Image(self.ring, image)
        return new

    def extension(self) -> L[S]:
        """"""
        pillow = self.ring.package.pillow

        dictionary = pillow.Image.registered_extensions()
        items = dictionary.items()
        values = pillow.Image.OPEN
        result = [key for key, value in items if value in values]
        result.sort()
        return result

    def __init__(self, ring, /, name, **star):
        super().__init__(ring, name, pypi="PIL")
        if self.package:
            setattr(self, "ImageTk", load.package("PIL", "ImageTk"))
