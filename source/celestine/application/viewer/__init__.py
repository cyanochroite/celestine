def argument(argument):
    parser = argument.subparser.add_parser(
        "demo",
        help="The default main application.",
    )

    return argument


def attribute():
    return []


def default():
    return []
