# https://pillow.readthedocs.io/en/stable/reference/Image.html
import PIL.Image as _Image


_Image.MAX_IMAGE_PIXELS = None


class Image:
    def __del__(self):
        self.height = None
        self.image = None
        self.ratio = None
        self.size = None
        self.width = None

    def __init__(self, image):
        self.height = image.height
        self.image = image
        self.ratio = image.width / image.height if image.height else 0
        self.size = image.size
        self.width = image.width

    @staticmethod
    def _float_to_integer(number):
        return int(round(number))

    @classmethod
    def new(cls, mode, x, y):
        mode = mode
        size = (x, y)
        color = 0
        return cls(_Image.new(mode, size, color))

    @classmethod
    def open(cls, path):
        fp = path
        mode = "r"
        formats = None
        return cls(_Image.open(fp, mode, formats))

    def convert(self, mode):
        matrix = None
        dither = _Image.NONE
        palette = 0
        colors = 256
        self.__init__(self.image.convert(mode, matrix, dither, palette, colors))

    @classmethod
    def old_png_convert(cls, load, save):
        base = cls.open(load)
        image = cls.old_from_input("RGB", base.size, 0)
        image.paste(base.image)
        image.save(save, "PNG")

    @staticmethod
    def old_from_input(mode, size, color):
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
        return _Image.new(mode, size, color)

    def resize(self, width, height):
        size = (self._float_to_integer(width), self._float_to_integer(height))
        resample = _Image.LANCZOS
        box = None
        reducing_gap = None
        self.__init__(self.image.resize(size, resample, box, reducing_gap))

    def resize_to_height(self, height):
        scale = height / self.height
        width = self.width * scale
        self.resize(width, height)

    def resize_to_width(self, width):
        scale = width / self.width
        height = self.height * scale
        self.resize(width, height)

    def rotate(self, rotation):
        angle = rotation
        resample = _Image.BICUBIC
        expand = True
        center = None
        translate = None
        fillcolor = None
        self.__init__(self.image.rotate(angle, resample, expand, center, translate, fillcolor))

    def save_jpg(self, path, quality=75, dpi=0):
        self._save_jpg(path, quality, True, False, dpi, dpi, None, bytes(), "4:4:4", None)

    def _save(self, fp, format, params):
        self.image.save(fp, format, **params)

    def _save_jpg(self, path, quality, optimize, progressive, x, y, icc_profile, exif, subsampling, qtables):
        fp = path
        format = "jpeg"
        params = {
            "quality": quality,
            "optimize": optimize,
            "progressive": progressive,
            "dpi": (x, y),
            "icc_profile": icc_profile,
            "exif": exif,
            "subsampling": subsampling,
            "qtables": qtables
        }
        self._save(fp, format, params)

####
    def save_png(self, path):
        print(_Image.SAVE)
        self.image.save(path, "PNG", optimize=True)
        print(_Image.SAVE)
        print(breakybreaky)

    def paste(self, image, x=0, y=0):
        im = image.image
        x = self._float_to_integer(x)
        y = self._float_to_integer(y)
        box = (x, y, x + image.width, y + image.height)
        mask = None
        self.image.paste(im, box, mask)

    @classmethod
    def my_convert(cls, load, save):
        base = cls.open(load)
        image = cls.from_input("RGB", base.size, 0)
        image.paste(base)
        image.save(save, "PNG")

    @classmethod
    def my_from_input(cls, mode, size, color):
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
        return _Image.new(mode, size, color)



