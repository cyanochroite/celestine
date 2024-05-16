""""""

import typing

from celestine.interface import View
from celestine.literal import FUNCTION
from celestine.typed import (
    B,
    C,
    N,
    R,
)

Call: typing.TypeAlias = C[[View], N]


def code(function: C[[R], B]) -> C[[R], B]:
    """"""

    def decorator(**star: R) -> B:
        return function(**star)

    return decorator


def scene(main: B | Call = False) -> C[[Call], N]:
    """"""

    def primary(function: Call) -> Call:
        """"""

        def decorator(view: View) -> N:
            function(view)

        return decorator

    def secondary(function: Call) -> Call:
        """"""

        def decorator(view: View) -> N:
            function(view)

        return decorator

    if str(main).startswith(FUNCTION):
        return secondary(main)

    return primary if main else secondary
