"""Python Imaging Library (Fork)."""

import math

from celestine import load
from celestine.window.collection import Plane
from celestine.typed import (
    IMAGE,
    LS,
    H,
    K,
    N,
    P,
    R,
    S,
)

from . import Abstract

########################################################################

COLORS = 15  # int(255 - 8 / 16)


class Image:
    """"""

    hold: H
    image: IMAGE

    def brightwing(self):
        """
        Brightwing no like the dark colors.

        Make image bright.
        """
        pillow = self.hold.package.pillow

        def brighter(pixel):
            invert = (255 - pixel) / 255
            boost = invert * 64
            shift = pixel + boost
            return shift

        hue, saturation, value = self.image.convert("HSV").split()
        new_value = value.point(brighter)

        bands = (hue, saturation, new_value)

        self.image = pillow.Image.merge("HSV", bands).convert("RGB")

    @classmethod
    def clone(cls, self) -> K:
        hold = self.hold
        image = self.image.copy()
        return cls(hold, image)

    def convert(self, mode: S) -> N:
        """"""
        pillow = self.hold.package.pillow

        matrix = None  # Unused default.
        dither = pillow.Image.Dither.FLOYDSTEINBERG
        palette = pillow.Image.Palette.WEB  # Unused default.
        colors = 256  # Unused default.

        hold = self.image.convert(mode, matrix, dither, palette, colors)
        self.image = hold

    def convert_to_alpha(self) -> N:
        """"""
        self.convert("RGBA")

    def convert_to_color(self) -> N:
        """"""
        self.convert("RGB")

    def convert_to_mono(self) -> N:
        """"""
        self.convert("1")

    def copy(self) -> K:
        return self.clone(self)

    def getdata(self):
        return self.image.getdata()

    def resize(self, size, box=None):
        """"""
        pillow = self.hold.package.pillow

        size_x, size_y = size

        size_x = max(1, round(size_x))
        size_y = max(1, round(size_y))

        size = (size_x, size_y)
        resample = pillow.Image.Resampling.LANCZOS
        reducing_gap = None

        hold = self.image.resize(size, resample, box, reducing_gap)
        self.image = hold

    def resize(self, size_x, size_y):
        """"""
        pillow = self.hold.package.pillow

        size = (size_x, size_y)
        resample = pillow.Image.Resampling.LANCZOS
        box = None
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

    def scale_to_fit(self, area: Plane):
        """"""
        pillow = self.hold.package.pillow

        curent = Plane.make(self.image.width, self.image.height)
        target = Plane.make(*area.size.int)

        result = curent.scale_to_min(target)
        # result = curent.scale_to_max(target)
        result.center(target)
        size = result.size

        best_x, best_y = size.int

        self.image = self.image.resize(
            size=(best_x, best_y),
            resample=pillow.Image.Resampling.LANCZOS,
            box=None,
            reducing_gap=None,
        )

        pillow = self.hold.package.pillow

    def scale_to_fill(self, area):
        """"""
        pillow = self.hold.package.pillow

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
        pillow = self.hold.package.pillow

        # Median Cut only works in RGB mode.
        self.convert_to_color()

        colors = COLORS
        method = pillow.Image.Quantize.MEDIANCUT
        kmeans = 0
        palette = None
        dither = pillow.Image.Dither.FLOYDSTEINBERG

        self.image = self.image.quantize(
            colors, method, kmeans, palette, dither
        )

    def __init__(self, hold: H, /, image: IMAGE, **star: R):
        self.hold = hold
        self.image = image


class Package(Abstract):
    """"""

    def new(self) -> Image:
        """"""
        pillow = self.hold.package.pillow

        mode = "RGBA"
        size = (100, 50)
        color = (250, 250, 250, 250)

        image = pillow.Image.new(mode, size, color)

        item = Image(self.hold, image)
        return item

    def open(self, path: P) -> Image:
        """"""
        pillow = self.hold.package.pillow

        file = pillow.Image.open(
            fp=path,
            mode="r",
            formats=None,
        )

        image = file.convert(
            mode="RGBA",
            matrix=None,
            dither=pillow.Image.Dither.NONE,
            palette=pillow.Image.Palette.ADAPTIVE,
            colors=256,
        )

        item = Image(self.hold, image)
        return item

    def extension(self) -> LS:
        """"""
        pillow = self.hold.package.pillow

        dictionary = pillow.Image.registered_extensions()
        items = dictionary.items()
        values = pillow.Image.OPEN
        result = [key for key, value in items if value in values]
        result.sort()
        return result

    def __init__(self, hold: H, /, name: S, **star: R) -> N:
        super().__init__(hold, name, pypi="PIL")
        if self.package:
            setattr(self, "ImageTk", load.package("PIL", "ImageTk"))
