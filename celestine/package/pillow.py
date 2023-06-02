""""""

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


########################################################################

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


def _quantize(self):
    """"""

    colors = 256
    method = None
    kmeans = 0
    palette = PALETTE
    dither = PIL.Image.Dither.NONE

    self.image = self.image.quantize(
        colors, method, kmeans, palette, dither
    )


########################################################################

COLORS = 15  # int(255 - 8 / 16)


class Image:
    def brightwing(self):
        """
        Brightwing no like the dark colors.

        Make image bright.
        """

        def brighter(pixel):
            invert = (255 - pixel) / 255
            boost = invert * 64
            shift = pixel + boost
            return shift

        hue, saturation, value = self.image.convert("HSV").split()
        new_value = value.point(brighter)

        bands = (hue, saturation, new_value)
        self.image = PIL.Image.merge("HSV", bands).convert("RGB")

    @classmethod
    def clone(cls, item):
        """"""
        image = item.image.copy()
        new = cls(image)
        return new

    def convert(self, mode):
        """"""

        matrix = None  # Unused default.
        dither = PIL.Image.Dither.FLOYDSTEINBERG
        palette = PIL.Image.Palette.WEB  # Unused default.
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

    @classmethod
    def load(cls, path):
        fp = path
        mode = "r"
        formats = None
        image = PIL.Image.open(fp, mode, formats)

        # Highest mode for median cut.
        mode = "RGB"
        matrix = None
        dither = PIL.Image.Dither.NONE
        palette = PIL.Image.Palette.ADAPTIVE
        colors = 256
        image = image.convert(mode, matrix, dither, palette, colors)

        new = cls(image)
        return new

    def resize(self, size_x, size_y, box=None):
        """"""

        size_x = max(1, round(size_x))
        size_y = max(1, round(size_y))

        size = (size_x, size_y)
        resample = PIL.Image.Resampling.LANCZOS
        reducing_gap = None

        hold = self.image.resize(size, resample, box, reducing_gap)
        self.image = hold

    @property
    def size(self):
        """"""
        return self.image.size

    def quantize(self):
        """"""

        colors = COLORS
        method = PIL.Image.Quantize.MEDIANCUT
        kmeans = 0
        palette = None
        dither = PIL.Image.Dither.FLOYDSTEINBERG

        self.image = self.image.quantize(
            colors, method, kmeans, palette, dither
        )

    def __init__(self, image):
        self.image = image
