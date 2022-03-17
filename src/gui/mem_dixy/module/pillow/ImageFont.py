# https://pillow.readthedocs.io/en/stable/reference/ImageFont.html
import PIL.ImageFont


class ImageFont():
    @staticmethod
    def truetype(font, size):
        font = font
        size = size
        index = 0
        encoding = "unic"
        layout_engine = PIL.ImageFont.LAYOUT_BASIC
        return PIL.ImageFont.truetype(font, size, index, encoding, layout_engine)
