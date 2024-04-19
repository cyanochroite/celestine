"""Python Imaging Library (Fork)."""

import random

from celestine import (
    bank,
    load,
)
from celestine.package.abstract import Abstract
from celestine.typed import (
    IMAGE,
    LI,
    LS,
    I,
    K,
    N,
    P,
    R,
    S,
    T,
)
from celestine.window.collection import (
    Plane,
    Point,
)

########################################################################

COLORS = 15  # int(255 - 8 / 16)


class Image:
    """"""

    image: IMAGE

    def brightwing(self):
        """
        Brightwing no like the dark colors.

        Make image bright.
        """

        def brighter(pixel: I) -> I:
            invert = (255 - pixel) / 255
            boost = invert * 64
            shift = pixel + boost
            return shift

        hue, saturation, value = self.image.convert("HSV").split()
        new_value = value.point(brighter)

        bands = (hue, saturation, new_value)

        merge = self.package.Image.merge("HSV", bands)
        self.image = merge.convert("RGB")

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        image = self.image.copy()
        return cls(image)

    def convert(self, mode: S) -> N:
        """"""
        matrix = None  # Unused default.
        dither = self.package.Image.Dither.FLOYDSTEINBERG
        palette = self.package.Image.Palette.WEB  # Unused default.
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
        """"""
        return self.clone(self)

    def getdata(self) -> LI:
        """"""
        return self.image.getdata()

    @property
    def size(self):
        """"""
        return self.image.size

    def resize(self, point: Point) -> N:
        """"""
        size = point.value
        resample = self.package.Image.Resampling.LANCZOS
        box = None
        reducing_gap = None
        self.image = self.image.resize(
            size,
            resample,
            box,
            reducing_gap,
        )

    def paste(self, image: K, plane: Plane) -> N:
        """"""
        im = image.image
        box = plane.value
        mask = None
        self.image.paste(im, box, mask)

    def quantize(self):
        """"""
        pillow = bank.self.package
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

    def __init__(self, image: IMAGE, **star: R):
        self.image = image


class Package(Abstract):
    """"""

    def new(self, size: T[I, I]) -> Image:
        """"""
        mode = "RGBA"
        color = (250, 250, 0, 250)
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            255,
        )

        image = self.package.Image.new(mode, size, color)

        item = Image(image)
        return item

    def open(self, path: P) -> Image:
        """"""
        file = self.package.Image.open(
            fp=path,
            mode="r",
            formats=None,
        )

        image = file.convert(
            mode="RGBA",
            matrix=None,
            dither=self.package.Image.Dither.NONE,
            palette=self.package.Image.Palette.ADAPTIVE,
            colors=256,
        )

        item = Image(image)
        return item

    def extension(self) -> LS:
        """"""
        dictionary = self.package.Image.registered_extensions()
        items = dictionary.items()
        values = self.package.Image.OPEN
        result = [key for key, value in items if value in values]
        result.sort()
        return result

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(name, pypi="PIL")
        if self.package:
            setattr(self, "ImageTk", load.package("PIL", "ImageTk"))
