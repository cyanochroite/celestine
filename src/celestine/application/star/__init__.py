"""Converts image to hashed png version."""
from celestine.application.star.image import Image
from celestine.application.star.hashlib import hashlib
from celestine.application.star.os import os

STORE = "store"
TODO = "todo"
DONE= "done"
STAR = "star"
NONE = ""

def argument(argument):
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


def default(configuration):
    configuration.set(STAR, TODO, "D:/todo")
    configuration.set(STAR, DONE, "D:/done")
    return configuration


def attribute(attribute):
    """Build up the attribute file."""
    return attribute.add("star", TODO, DONE)
