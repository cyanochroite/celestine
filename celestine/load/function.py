"""Central place for loading and importing external files."""

from typing import TypeAlias as TA

from celestine.typed import (
    CA,
    LS,
    MT,
    D,
    N,
    S,
)

from .data import FUNCTION

FN: TA = CA[[N], N]


def load(module: MT) -> D[S, FN]:
    """Load from module all functions and turn them into dictionary."""
    dictionary = vars(module)
    iterable = {
        key: value
        for key, value in dictionary.items()
        if repr(value).startswith(FUNCTION)
    }
    return iterable


def function_page(module: MT) -> LS:
    """Load from module all functions and turn them into dictionary."""

    dictionary = load(module)
    iterable = [key for key, value in dictionary.items()]
    return iterable
