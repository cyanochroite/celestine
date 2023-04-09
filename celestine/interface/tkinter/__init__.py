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
        ".pbm",
        ".pgm",
        ".ppm",
        ".pnm",
        ".gif",
        ".png",
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
