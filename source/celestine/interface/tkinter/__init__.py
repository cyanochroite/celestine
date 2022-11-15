from .window import Window


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
