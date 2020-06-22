import PIL.Image
import os


class mem_image:
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

    def __init__(self, image):
        self.image = image

    @classmethod
    def from_path(cls, path):
        fp = path.path
        mode = "r"
        image = PIL.Image.open(fp, mode)
        return cls(image)

    @classmethod
    def from_input(cls, mode, size, color):
        if mode not in mem_image.modes:
            raise ValueError("Invalid value for 'mode' variable.")
        image = PIL.Image.new(mode, size, color)
        return cls(image)

    def new_RGB(x, y):
        mode = "RGBA"
        size = (x, y)
        color = (0x00, 0x00, 0x00)
        return mem_image._new(mode, size, color)

    def new_RGBA(x, y):
        mode = "RGBA"
        size = (x, y)
        color = (0x00, 0x00, 0x00, 0x00)
        return mem_image._new(mode, size, color)

    def paste(self, them):
        self.image.paste(them.image)

    def save(self, path, format):
        fp = path.path
        self.image.save(fp, format)

    def image_save(image, path):  # {
        if os.path.isfile(path):  # {
            os.remove(path)
        # }
        with open(path, "wb") as file:  # {
            mem_image.save(file, "PNG", optimize=True)
        # }
    # }

    def file_save(load_file):  # {
        load_path = ".\\"
    #    load_file = "bleach_yachiru0035-1.jpg";
        save_path = ".\\"
        save_file = "demo.png"
        base = image_open(load_path + load_file)
        image = image_new(base.size)
        image.paste(base)
        image_save(image, save_path + save_file)
