"""Load and save user settings from a file."""

CONFIGURE = "configure"

DIRECTORY = "directory"
TASK = "task"

VIEWER = "viewer"


def argument(argument):
    """Build up the argument."""
    parser = argument.subparser.add_parser(
        "viewer",
        help="The default main application.",
    )

    parser.add_argument(
        argument.flag(DIRECTORY),
        argument.name(DIRECTORY),
    )

    configure = argument.subparser.add_parser(
        "viewer_configure",
        # CONFIGURE,
        help="you are a fish",
    )

    return argument


def default():
    """Build up the default file."""
    return ["main"]


def attribute():
    """Build up the attribute file."""
    return ["task"]

