import PIL.Image


class Image():
    @classmethod
    def open(cls, Path):
        fp = Path
        mode = "r"
        return PIL.Image.open(fp, mode)

    @classmethod
    def from_input(cls, mode, size, color):
        """Pillow 7.0.0"""
        modes = {
            "1",  # (1-bit pixels, black and white, stored with one pixel per byte)
            "L",  # (8-bit pixels, black and white)
            "P",  # (8-bit pixels, mapped to any other mode using a color palette)
            "RGB",  # (3x8-bit pixels, true color)
            "RGBA",  # (4x8-bit pixels, true color with transparency mask)
            "CMYK",  # (4x8-bit pixels, color separation)
            "YCbCr",  # (3x8-bit pixels, color video format)
            "LAB",  # (3x8-bit pixels, the L*a*b color space)
            "HSV",  # (3x8-bit pixels, Hue, Saturation, Value color space)
            "I",  # (32-bit signed integer pixels)
            "F",  # (32-bit floating point pixels)
        }
        if mode not in modes:
            raise ValueError("Invalid value for 'mode' variable.")
        return PIL.Image.new(mode, size, color)
