import argparse
import sys

VERSION = 1

option = [
    "a",
    "b"
]

#https://docs.python.org/3/library/argparse.html
class Window():
    def run(self, setup, view):
        print(sys.argv)
        data = sys.argv[3:]
        print(sys.argv)
        parser = argparse.ArgumentParser(
            prog="celestine"
        )
        
        parser.add_argument(
            "option",
            nargs="?",
            default="a",
            choices=option,
            help="Choose a mode to opperate in."
        )
    
        parse = parser.parse_args(sys.argv[3:])
        mode = parse.option
        mode = 'a'
        if data:
            mode = data[0]
        print(mode)
    
        if mode == "a":
            print("Hello World")

        if mode == "b":
            print("Goodby Island")
