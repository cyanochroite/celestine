"""Package dearpygui."""
from celestine.application.dearpygui.window import Window


def argument(arguments):
    """Build up the argument."""
    return arguments


def attribute():
    """Build up the attribute file."""
    return ()


def default():
    """Build up the default file."""
    return ()


def image_format():
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
    return Window(session)
