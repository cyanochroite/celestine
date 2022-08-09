"""Package tkinter."""
TASK = "task"
TKINTER = "tkinter"
def argument(argument):
    window = argument.subparser.add_parser(
        "window",
        help="you are a fish",
    )

    return argument

def configuration(configuration, task="main"):
    """Build up the configuration file."""
    configuration.set(TKINTER, TASK, task)
    return configuration


    return configuration


