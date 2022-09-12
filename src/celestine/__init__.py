""""this is a package"""
from celestine.session import Session


def main(directory, argv, exit_on_error):
    """Run the main program."""
    session = Session(directory, argv, exit_on_error)
    return session.main()
