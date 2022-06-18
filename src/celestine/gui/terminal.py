# https://docs.python.org/3/library/argparse.html
import argparse
import sys

VERSION = 1

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
        parser.add_argument("-g", "--gui")
        parser.add_argument(
            "option",
            nargs="?",
            default="a",
            choices=option,
            help="Choose a mode to opperate in."
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
