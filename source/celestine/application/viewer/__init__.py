DIRECTORY = "directory"


def argument(argument):
    argument.parser.add_argument(
        argument.flag(DIRECTORY),
        argument.name(DIRECTORY),
    )

    return argument


def attribute():
    return []


def default():
    return []
