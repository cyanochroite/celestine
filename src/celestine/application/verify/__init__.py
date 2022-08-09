"""Package unittest."""
def argument(argument):
    
    window = argument.subparser.add_parser(
        "main",
        default="main",
        help="you are a fish",
    )

    return argument

def configuration(configuration):
    """Build up the configuration file."""
    return configuration


