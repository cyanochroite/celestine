""""""

from enum import Enum

from celestine.interface import View
from celestine.literal import FUNCTION
from celestine.typed import (
    C,
    N,
    R,
)


class State(Enum):
    """"""

    CODE = 1
    VIEW = 2


def main(function: C[[View], N]) -> C[[View], N]:
    """"""

    def decorator(view: View) -> N:
        function(view)

    return decorator


def scene(function):
    """"""

    def decorator(view: View) -> N:
        function(view)

    return decorator


def code(function: C[[View], N]) -> C[[View], N]:
    """"""

    def decorator(**star: R) -> N:
        function(**star)

    return decorator


def scene(function):
    """"""

    def decorator(view: View) -> N:
        function(view)

    return decorator


print("A!")


def scene(value=False):
    """"""

    def main(function: C[[View], N]) -> C[[View], N]:
        """"""

        def decorator(view: View) -> N:
            function(view)

        return decorator

    def view(function: C[[View], N]) -> C[[View], N]:
        """"""

        def decorator(view: View) -> N:
            function(view)

        return decorator

    if str(value).startswith(FUNCTION):
        return view(value)

    return main if value else view
