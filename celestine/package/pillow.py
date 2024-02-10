"""Python Imaging Library (Fork)."""

import random

from celestine import load
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
from celestine.window.collection import (
    Plane,
    Point,
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

    @property
    def size(self):
        """"""
        return self.image.size

    def resize(self, point: Point) -> N:
        pillow = self.hold.package.pillow

        size = point.int
        resample = pillow.Image.Resampling.LANCZOS
        box = None
        reducing_gap = None
        self.image = self.image.resize(
            size,
            resample,
            box,
            reducing_gap,
        )

    def paste(self, image: K, plane: Plane) -> N:
        im = image.image
        box = plane.int
        mask = None
        self.image.paste(im, box, mask)

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

    def new(self, size) -> Image:
        """"""
        pillow = self.hold.package.pillow

        mode = "RGBA"
        color = (250, 250, 0, 250)
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            255,
        )

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
