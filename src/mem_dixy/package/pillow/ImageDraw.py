# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
import PIL.ImageDraw as _ImageDraw


class ImageDraw():
    @staticmethod
    def Draw(image):
        im = image
        mode = None
        return _ImageDraw.Draw(im, mode)
