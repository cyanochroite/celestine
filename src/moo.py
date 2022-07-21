"""Load and save user settings from a file."""

import os.path
import sys
import keyword
import shutil

directory = sys.path[0]


from celestine.keyword.main import WRITE



def reset():
    path = os.path.join(directory, "celestine", "language")
    if os.path.islink(path):
        raise RuntimeError
    
    if os.path.isdir(path):
        shutil.rmtree.avoids_symlink_attacks
        shutil.rmtree(path, ignore_errors=False, onerror=None)
    
    os.mkdir(path)
    
    
def header():
    path = os.path.join(directory, "celestine", "language", "__init__.py")
    with open(path, WRITE) as file:
        file.write(F'"""Lookup table for languages."""\n')


reset()
header()


def format_line(name, value):
    if not name.isidentifier():
        raise ValueError("Not a valid identifier.")
    if keyword.iskeyword(name) or keyword.issoftkeyword(name):
        raise ValueError("This work is a keyword.")
    value = value.replace('"', "'")
    return F'{name} = "{value}"\n'

language = "friday"
path = os.path.join(directory, "celestine", "language", "monkey.py")
names = ['sugar', 'spice', 'everything_nice']
values = ["1", "2", "3"]
with open(path, WRITE) as file:
    file.write(F'"""Lookup table for {language}."""\n')
    file.writelines(map(format_line, names, values))

