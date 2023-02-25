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
from celestine.unicode import LOW_LINE

from .text import FUNCTION

F: TA = CA[[N], N]


def function(module: MT) -> D[S, F]:
    """
    Load from module all functions and turn them into dictionary.
    """
    dictionary = vars(module)
    iterable = {
        key: value
        for key, value in dictionary.items()
        if repr(value).startswith(FUNCTION)
        and not key.startswith(LOW_LINE)
    }
    return iterable


def function_name(module: MT) -> L[S]:
    """
    Load from module all functions and turn them into dictionary.
    """

    dictionary = function(module)
    iterable = [key for key, value in dictionary.items()]
    return iterable


def function_value(module: MT) -> L[F]:
    """
    Load from module all functions and turn them into dictionary.
    """
    dictionary = function(module)
    iterable = [value for key, value in dictionary.items()]
    return iterable
