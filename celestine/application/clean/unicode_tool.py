"""
This is a modified main file, so might not run as application.

Converts the Unicode text file into a python dictionary.
Was run from the project root.
"""
import os
import sys

sys.path[0] = os.path.dirname(sys.path[0])


from celestine import load
from celestine.file import (
    open_file,
    save_module,
)


def work(document):
    for line in document:
        strip = line.strip()
        split = strip.split(";")

        number = split[0]
        number = int(number, 16)

        name = split[1]
        if name == "<control>":
            name = split[10]
            if name == "":
                # U+0099
                name = "Single Graphic Character Introducer"

        elif name[0] == "<":
            continue

        name = name.split("(")[0]
        name = name.strip()

        name = name.replace(" ", "_")
        name = name.replace("-", "_")

        text = f"{name} = chr({number})\n"

        yield text


file = load.pathway("UnicodeData.txt")
load = open_file(file)
text = work(load)
save_module(text, "unicode")
