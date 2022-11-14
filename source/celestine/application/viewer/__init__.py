from celestine.session import load


def main(_):
    """Run the main program."""
    window = load.module("application", "viewer", "window")
    application = [
        # module.main,
        window.zero,
        window.one,
        window.two,
    ]
    return application
