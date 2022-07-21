"""Load and save user settings from a file."""

import os.path
import sys
import keyword

directory = sys.path[0]

import configparser


from celestine.keyword.main import CONFIGURATION_CELESTINE
from celestine.keyword.main import ENCODING
from celestine.keyword.main import ERRORS
from celestine.keyword.main import READ
from celestine.keyword.main import WRITE


def file_mode(file, mode):
    buffering = 1
    encoding = ENCODING
    errors = ERRORS
    newline = None
    closefd = True
    opener = None
    return open(
        file,
        mode,
        buffering,
        encoding,
        errors,
        newline,
        closefd,
        opener
    )


language = "italian"
data = "a puppy"
candy = [
    F'"""Lookup table for {language}."""\n',
    F'eat_peppers = "{data}"\n'
]
path = os.path.join(directory, "monkey.py")


def format_line(name, value):
    if not name.isidentifier():
        raise ValueError("Not a valid identifier.")
    if keyword.iskeyword(name) or keyword.issoftkeyword(name):
        raise ValueError("This work is a keyword.")
    value = value.replace('"', "'")
    return F'{name} = "{value}"\n'


names = ['sugar', 'spice', 'everything_nice']
values = ["1", "2", "3"]
with file_mode(path, WRITE) as file:
    file.write(F'"""Lookup table for {language}."""\n')
    file.writelines(map(format_line, names, values))


print("cow")







names = ['sugar', 'spice', 'everything_nice']
values = ["1", "2", "3"]

fish = map(format_line, names, values)

print(list(fish))

