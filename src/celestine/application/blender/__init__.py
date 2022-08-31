"""Package blender."""


def argument(argument):
    """Build up the argument."""
    verify = argument.subparser.add_parser(
        "verify",
        help="you are a fish",
    )
    
    return argument


def attribute():
    """Build up the attribute file."""
    return ()


def default():
    """Build up the default file."""
    return ()


def image_format():
    return [
        ".bmp",
        ".sgi",
        ".rgb",
        ".bw",
        ".png",
        ".jpg",
        ".jpeg",
        ".jp2",
        ".j2c",
        ".tga",
        ".cin",
        ".dpx",
        ".exr",
        ".hdr",
        ".tif",
        ".tiff",
        ".webp",
    ]
