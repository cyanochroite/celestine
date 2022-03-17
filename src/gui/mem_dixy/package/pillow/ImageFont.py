# https://pillow.readthedocs.io/en/stable/reference/ImageFont.html
import PIL.ImageFont as _ImageFont


class ImageFont():
    @staticmethod
    def truetype(font, size):
        font = font
        size = size
        index = 0
        encoding = "unic"
        layout_engine = _ImageFont.LAYOUT_BASIC
        return _ImageFont.truetype(font, size, index, encoding, layout_engine)
