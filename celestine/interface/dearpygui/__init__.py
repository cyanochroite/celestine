""""""

from .element import (
    Button,
    Image,
    Label,
)
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


def window(session, **star):
    """"""
    element = {
        "button": Button,
        "image": Image,
        "label": Label,
    }
    size = (1280, 1080)
    return Window(session, element, size, **star)
