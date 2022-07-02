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

parse = load_module("core", "argparse").parser()
session = load_module("data", "session").Session(directory, parse)
window = load_module("package", session.package).Window()
run = load_module("window", "main").main(session)

window.run(run)

sys.exit()
