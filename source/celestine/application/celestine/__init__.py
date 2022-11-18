"""Load and save user settings from a file."""

CONFIGURE = "configure"

DIRECTORY = "directory"
TASK = "task"


def argument(argument):
    """Build up the argument."""
    argument.parser.add_argument(
        argument.flag(DIRECTORY),
        argument.name(DIRECTORY),
    )

    return argument


def default():
    """Build up the default file."""
    return ["main"]


def attribute():
    """Build up the attribute file."""
    return ["task"]

