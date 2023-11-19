"""Central place for loading and importing external files."""

from celestine.typed import (
    FN,
    LS,
    D,
    M,
    S,
    string,
)
from celestine.unicode import FULL_STOP

from .data import FUNCTION


def load(module: M) -> D[S, FN]:
    """Load from module all functions and turn them into dictionary."""
    dictionary = vars(module)
    iterable = {
        key: value
        for key, value in dictionary.items()
        if FUNCTION in repr(value)
    }
    return iterable


def decorator_name(module: M, name: S) -> S:
    """Load from module all functions and turn them into dictionary."""
    dictionary = vars(module)
    text = string(FUNCTION, name, FULL_STOP)
    for key, value in dictionary.items():
        if text in repr(value):
            return key
    raise LookupError("No function with '@main' found.")


def decorators(module: M, name: S) -> D[S, FN]:
    """Load from module all functions and turn them into dictionary."""
    dictionary = vars(module)
    text = string(FUNCTION, name, FULL_STOP)
    iterable = {
        key: value
        for key, value in dictionary.items()
        if text in repr(value)
    }
    return iterable


def function_page(module: M) -> LS:
    """Load from module all functions and turn them into dictionary."""

    dictionary = load(module)
    iterable = [key for key, value in dictionary.items()]
    return iterable
