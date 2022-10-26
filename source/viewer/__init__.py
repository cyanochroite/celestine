import celestine

from viewer import main as module


def main(directory, argv, exit_on_error):
    """Run the main program."""
    window = [
        # module.main,
        module.zero,
        module.one,
        module.two,
    ]
    celestine.main(directory, argv, exit_on_error, window)
