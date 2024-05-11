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


def code(function: C[[View], N]) -> C[[View], N]:
    """"""

    def decorator(**star: R) -> N:
        function(**star)

    return decorator


def scene(primary_window=False) -> C[[C[[View], N]], N]:
    """"""

    def primary(function: C[[View], N]) -> C[[View], N]:
        """"""

        def decorator(view: View) -> N:
            function(view)

        return decorator

    def secondary(function: C[[View], N]) -> C[[View], N]:
        """"""

        def decorator(view: View) -> N:
            function(view)

        return decorator

    if str(primary_window).startswith(FUNCTION):
        return secondary(primary_window)

    return primary if primary_window else secondary
