"""Converts image to hashed png version."""
from celestine.application.star.image import Image
from celestine.application.star.hashlib import hashlib
from celestine.application.star.os import os

STORE = "store"
TODO = "todo"
DONE = "done"
STAR = "star"
NONE = ""


def argument(argument):
    """Build up the argument."""
    main = argument.main

    main.add_argument(
        TODO,
        action=STORE,
        help="A brief description of what the argument does.",
    )

    main.add_argument(
        DONE,
        action=STORE,
        help="A brief description of what the argument does.",
    )
    return argument


def attribute():
    """Build up the attribute file."""
    return (TODO, DONE)


def default():
    """Build up the default file."""
    return ("D:/todo", "D:/done")


def image_format():
    return []
