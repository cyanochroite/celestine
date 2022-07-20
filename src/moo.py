"""Load and save user settings from a file."""

import os.path
import sys

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
with file_mode(path, WRITE) as file:
    file.writelines(candy)

print("cow")