"""Python Imaging Library (Fork)."""

import math

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

    def convert_to_alpha(self):
        """"""
        self.convert("RGBA")

    def convert_to_color(self):
        """"""
        self.convert("RGB")

    def convert_to_mono(self):
        """"""

        self.convert("1")

    def getdata(self):
        return self.image.getdata()

    def resize(self, size, box=None):
        """"""
        pillow = self.ring.package.pillow

        size_x, size_y = size

        size_x = max(1, round(size_x))
        size_y = max(1, round(size_y))

        size = (size_x, size_y)
        resample = pillow.Image.Resampling.LANCZOS
        reducing_gap = None

        hold = self.image.resize(size, resample, box, reducing_gap)
        self.image = hold

    def scale_to_any(self, area, crop=False):
        """"""
        (size_x, size_y) = self.size
        (area_x, area_y) = area

        down_x = math.floor(area_y * size_x / size_y)
        down_y = math.floor(area_x * size_y / size_x)

        if crop:
            best_x = max(area_x, down_x)
            best_y = max(area_y, down_y)
        else:
            best_x = min(area_x, down_x)
            best_y = min(area_y, down_y)

        return (best_x, best_y)

    def scale_to_fit(self, area):
        """"""
        pillow = self.ring.package.pillow

        (size_x, size_y) = self.size
        (area_x, area_y) = area

        down_x = math.floor(area_y * size_x / size_y)
        down_y = math.floor(area_x * size_y / size_x)

        best_x = min(area_x, down_x)
        best_y = min(area_y, down_y)

        self.image = self.image.resize(
            size=(best_x, best_y),
            resample=pillow.Image.Resampling.LANCZOS,
            box=None,
            reducing_gap=None,
        )

    def scale_to_fill(self, area):
        """"""
        pillow = self.ring.package.pillow

        (size_x, size_y) = self.size
        (area_x, area_y) = area

        down_x = math.floor(area_y * size_x / size_y)
        down_y = math.floor(area_x * size_y / size_x)

        best_x = max(area_x, down_x)
        best_y = max(area_y, down_y)

        length_x = round(area_x / best_x * size_x)
        length_y = round(area_y / best_y * size_y)

        offset_x = round((size_x - length_x) / 2)
        offset_y = round((size_y - length_y) / 2)
        cutoff_x = offset_x + length_x
        cutoff_y = offset_y + length_y

        self.image = self.image.resize(
            size=(area_x, area_y),
            resample=pillow.Image.Resampling.LANCZOS,
            box=(offset_x, offset_y, cutoff_x, cutoff_y),
            reducing_gap=None,
        )

    @property
    def size(self):
        """"""
        return self.image.size

    def quantize(self):
        """"""
        pillow = self.ring.package.pillow

        # Median Cut only works in RGB mode.
        self.convert_to_color()

        colors = COLORS
        method = pillow.Image.Quantize.MEDIANCUT
        kmeans = 0
        palette = None
        dither = pillow.Image.Dither.FLOYDSTEINBERG

        self.image = self.image.quantize(colors, method, kmeans, palette, dither)

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
        mode = "RGBA"
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
