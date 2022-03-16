# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
import PIL.ImageDraw


class ImageDraw():
    @staticmethod
    def Draw(image):
        im = image
        mode = None
        return PIL.ImageDraw.Draw(im, mode)
