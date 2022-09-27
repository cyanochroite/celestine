"""Package tkinter."""
from celestine.application.tkinter.window import Window


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
        ".pbm",
        ".pgm",
        ".ppm",
        ".pnm",
        ".gif",
        ".png",
    ]


def window(session):
    return Window(session)
