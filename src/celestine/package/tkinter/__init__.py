from .window import Window


def argument(arguments):
    return arguments


def attribute():
    return ()


def default():
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
