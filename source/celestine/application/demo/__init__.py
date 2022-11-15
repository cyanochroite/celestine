"""Load and save user settings from a file."""

CONFIGURE = "configure"

DIRECTORY = "directory"
TASK = "task"


def argument(argument):
    """Build up the argument."""
    argument.main = argument.subparser.add_parser(
        "main",
        help="The default main application.",
    )

    argument.main.add_argument(
        argument.flag(DIRECTORY),
        argument.name(DIRECTORY),
    )

    configure = argument.subparser.add_parser(
        CONFIGURE,
        help="you are a fish",
    )

    return argument


def default():
    """Build up the default file."""
    return ["main"]


def attribute():
    """Build up the attribute file."""
    return ["task"]

