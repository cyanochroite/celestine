"""Central place for loading and importing external files."""

from celestine.typed import (
    LS,
    C,
    D,
    M,
    N,
    S,
    FN,
)

from .data import FUNCTION


def load(module: M) -> D[S, FN]:
    """Load from module all functions and turn them into dictionary."""
    dictionary = vars(module)
    iterable = {
        key: value
        for key, value in dictionary.items()
        if repr(value).startswith(FUNCTION)
    }
    return iterable


def function_page(module: M) -> LS:
    """Load from module all functions and turn them into dictionary."""

    dictionary = load(module)
    iterable = [key for key, value in dictionary.items()]
    return iterable
