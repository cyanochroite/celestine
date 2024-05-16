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

    def __call__(self, **star: R) -> B:
        ...


class Scene(Protocol):
    """Type for code functions."""

    def __call__(self, view: View) -> N:
        ...


class SuperScene(Protocol):
    """Type for code functions."""

    def __call__(self, function: Scene) -> Scene:
        ...


def code(function: Code) -> Code:
    """"""

    def decorator(**star: R) -> B:
        return function(**star)

    return decorator


def scene(main: B | Scene = False) -> Scene | SuperScene:
    """"""

    def primary(function: Scene) -> Scene:
        """"""

        def decorator(view: View) -> N:
            return function(view)

        return decorator

    def secondary(function: Scene) -> Scene:
        """"""

        def decorator(view: View) -> N:
            return function(view)

        return decorator

    if not isinstance(main, B):
        return secondary(main)

    return primary if main else secondary
