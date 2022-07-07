"""This is the main file. It runs first."""
import os.path
import sys

directory = sys.path[0] = os.path.dirname(sys.path[0])
sys.path.append(directory)


def load_module(*paths):
    """Load an internal module from anywhere in the application."""
    iterable = ["celestine"] + list(paths)
    name = ".".join(iterable)
    item = __import__(name)
    for path in paths:
        item = getattr(item, path)
    return item


argument = load_module("main", "argument").argument
configuration = load_module("main", "configuration").more(directory, argument)
session = load_module("main", "session").Session(argument, configuration)
main = load_module("window", "main").main(session)

session.package.Window(session).run(main)

sys.exit()
