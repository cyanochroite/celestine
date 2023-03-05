"""Central place for loading and importing external files."""

from typing import TypeAlias as TA

from celestine.typed import (
    CA,
    MT,
    D,
    L,
    N,
    S,
)

from .text import FUNCTION

FN: TA = CA[[N], N]


def load(module: MT) -> D[S, FN]:
    """
    Load from module all functions and turn them into dictionary.
    """
    dictionary = vars(module)
    iterable = {
        key: value
        for key, value in dictionary.items()
        if repr(value).startswith(FUNCTION)
    }
    return iterable


def find(dictionary: D[S, FN], prefix: S) -> D[S, FN]:
    """Filter the dictionary based on a name."""
    iterable = {
        key: value
        for key, value in dictionary.items()
        if key.startswith(prefix)
    }
    return iterable


def function_page(module: MT) -> L[S]:
    """
    Load from module all functions and turn them into dictionary.
    """

    dictionary = load(module)
    iterable = [key for key, value in dictionary.items()]
    return iterable


