""""""

from celestine.interface import View
from celestine.literal import FUNCTION
from celestine.typed import (
    B,
    C,
    N,
    R,
)


def code(function: C[[View], N]) -> C[[View], N]:
    """"""

    def decorator(**star: R) -> N:
        function(**star)

    return decorator


def scene(primary_window: B = False) -> C[[C[[View], N]], N]:
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
