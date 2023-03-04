""""""
from .window import Window


def image_format():
    """"""
    return [
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp",
        ".gif",
        ".hdr",
        ".pic",
        ".pbm",
        ".pgm",
        ".ppm",
        ".pnm",
    ]


def window(session):
    """"""
    return Window(session)
