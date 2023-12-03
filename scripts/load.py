""""""

import os
import pathlib

type N = None
type P = pathlib.Path


def clamp(minimum, midterm, maximum):
    """The order of the inputs actually don't matter."""
    return sorted((minimum, midterm, maximum))[1]


def remove_empty_directories(path: P) -> N:
    """"""
    empty = True
    for content in path.iterdir():
        if content.is_dir():
            empty &= remove_empty_directories(content)
        else:
            empty = False
    if empty:
        os.rmdir(path)
    return empty
