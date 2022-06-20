# https://docs.python.org/3/library/argparse.html
import argparse
import sys

VERSION = 1


STORE = "store"
STORE_CONST = "store_const"
STORE_TRUE = "store_true"
STORE_FALSE = "store_false"
APPEND = "append"
APPEND_CONST = "append_const"
COUNT = "count"
HELP = "help"
VERSION = "version"
EXTEND = "extend"


option = [
    "a",
    "b",
    "list"
]


class Window():
    def __init__(self):
        self.list = []

    def label_add(self, image):
        pass

    def image_load(self, file):
        self.list.append(file)

    def run(self, setup, view):
        parser = argparse.ArgumentParser(prog="celestine")

        parser.add_argument(
            "-p", "--package",
            action="store_true",
            help="List all installed packages."
        )

        parser.add_argument(
            "-m", "--mode",
            default=MAIN,
            choices=MODE,
            help="Choose a mode to opperate in."
        )
        
        parser.add_argument(
            "-i", "--ini",
            action=STORE,
            nargs=1,
            help="List all installed packages."
        )
        
        parse = parser.parse_args()
        mode = parse.option

        setup(self)
        view(self)

        if mode == "a":
            print("Hello World")

        if mode == "b":
            print("Goodby Island")

        if mode == "list":
            print("here is a list")
            print(self.list)

