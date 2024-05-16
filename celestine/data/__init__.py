""""""

from celestine.interface import View
from celestine.literal import FUNCTION
from celestine.typed import (
    B,
    C,
    N,
    R,
)


def code(function: C[[R], B]) -> C[[R], B]:
    """"""

    def decorator(**star: R) -> B:
        return function(**star)

    return decorator


def scene(main: B = False) -> C[[C[[View], N]], N]:
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

    if str(main).startswith(FUNCTION):
        return secondary(main)

    return primary if main else secondary
