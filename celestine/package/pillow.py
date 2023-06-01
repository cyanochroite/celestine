""""""

import PIL
import PIL.Image

palettedata = [
    0x00,
    0x0F,
    0x1E,
    0x2D,
    0x3C,
    0x4B,
    0x5A,
    0x69,
    0x78,
    0x87,
    0x96,
    0xA5,
    0xB4,
    0xC3,
    0xD2,
    0xE1,
    0xF0,
    0xFF,
]

TERMINAL_RATIO = 15 / 7

ASCII_CHARS = [
    "@",
    "$",
    "&",
    "#",
    "%",
    "?",
    "*",
    "=",
    "+",
    '"',
    "!",
    "^",
    ";",
    "-",
    ",",
    "'",
    "`",
    ".",
]


######

PALETTE = PIL.Image.new("P", (1, 1))
PALETTE.putpalette(
    [
        0x00,
        0x00,
        0x00,
        0x0F,
        0x0F,
        0x0F,
        0x1E,
        0x1E,
        0x1E,
        0x2D,
        0x2D,
        0x2D,
        0x3C,
        0x3C,
        0x3C,
        0x4B,
        0x4B,
        0x4B,
        0x5A,
        0x5A,
        0x5A,
        0x69,
        0x69,
        0x69,
        0x78,
        0x78,
        0x78,
        0x87,
        0x87,
        0x87,
        0x96,
        0x96,
        0x96,
        0xA5,
        0xA5,
        0xA5,
        0xB4,
        0xB4,
        0xB4,
        0xC3,
        0xC3,
        0xC3,
        0xD2,
        0xD2,
        0xD2,
        0xE1,
        0xE1,
        0xE1,
        0xF0,
        0xF0,
        0xF0,
        0xFF,
        0xFF,
        0xFF,
    ]
)


class Image:
    def convert(self, mode):
        """"""

        matrix = None
        dither = PIL.Image.Dither.NONE
        palette = PIL.Image.Palette.WEB
        colors = 256

        self.image = self.image.convert(
            mode, matrix, dither, palette, colors
        )

    def getdata(self):
        return self.image.getdata()

    def resize(self, width, height):
        """"""

        width = max(1, round(width))
        height = max(1, round(height))

        size = (width, height)
        resample = PIL.Image.Resampling.LANCZOS
        box = None
        reducing_gap = None

        self.image = self.image.resize(
            size, resample, box, reducing_gap
        )

    @property
    def size(self):
        """"""
        return self.image.size

    def quantize(self):
        """"""

        colors = 256
        method = None
        kmeans = 0
        palette = PALETTE
        dither = PIL.Image.Dither.NONE

        self.image = self.image.quantize(
            colors, method, kmeans, palette, dither
        )

    def __init__(self, path):
        fp = path
        mode = "r"
        formats = None

        self.image = PIL.Image.open(fp, mode, formats)


class Mono:
    def convert(self):
        """"""

        mode = "1"
        matrix = None  # Unused default.
        dither = PIL.Image.Dither.FLOYDSTEINBERG
        palette = PIL.Image.Palette.WEB  # Unused default.
        colors = 256  # Unused default.

        hold = self.image.convert(mode, matrix, dither, palette, colors)
        self.image = hold

    def getdata(self):
        return self.image.getdata()

    def resize(self, width, height, box):
        """"""
        size = (width, height)
        resample = PIL.Image.Resampling.LANCZOS
        reducing_gap = None  # Unused default.

        hold = self.image.resize(size, resample, box, reducing_gap)
        self.image = hold

    @property
    def size(self):
        """"""
        return self.image.size

    def __init__(self, path):
        fp = path
        mode = "r"
        formats = None

        self.image = PIL.Image.open(fp, mode, formats)




class Color(Mono):
    def convert(self):
        """"""

        mode = "RGB"
        matrix = None  # Unused default.
        dither = PIL.Image.Dither.FLOYDSTEINBERG
        palette = PIL.Image.Palette.WEB  # Unused default.
        colors = 256  # Unused default.

        hold = self.image.convert(mode, matrix, dither, palette, colors)
        self.image = hold

