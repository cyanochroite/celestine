"""This is the main file. It runs first."""
import os.path
import sys

directory = os.path.dirname(sys.path[0])
sys.path.append(directory)


def load_module(*paths):
    """Load an internal module from anywhere in the application."""
    iterable = ["celestine"] + list(paths)
    name = ".".join(iterable)
    item = __import__(name)
    for path in paths:
        item = getattr(item, path)
    return item


parser = load_module("main", "argument").parser
argument = parser.parse_args()

session = load_module("main", "session").Session(argument, directory)
main = load_module("window", "main").main(session)

session.application.main(session=session, window=main)

sys.exit()
