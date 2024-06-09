""""""

from typing import Protocol

from celestine.interface import View
from celestine.typed import (
    B,
    N,
    R,
)


class Code(Protocol):
    """Type for code functions."""

    def __call__(self, **star: R) -> B: ...


class Draw(Protocol):
    """Type for code functions."""

    def __call__(self, view: View) -> N: ...


def call(function: Code) -> Code:
    """"""

    def decorator(**star: R) -> B:
        return function(**star)

    return decorator


def draw(function: Draw) -> Draw:
    """"""

    def decorator(view: View) -> N:
        return function(view)

    return decorator


def main(function: Draw) -> Draw:
    """"""

    def decorator(view: View) -> N:
        return function(view)

    return decorator
