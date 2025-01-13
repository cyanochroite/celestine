""""""

from celestine import (
    bank,
    load,
    regex,
)
from celestine.interface import View
from celestine.literal import FULL_STOP
from celestine.typed import (
    A,
    B,
    C,
    N,
    Protocol,
    R,
    S,
)


class Code(Protocol):
    """Type for code functions."""

    def __call__(self, **star: R) -> B:
        raise NotImplementedError(self, star)


class Draw(Protocol):
    """Type for draw functions."""

    def __call__(self, view: View) -> N:
        raise NotImplementedError(self, view)


class Wrapper(Protocol):
    """Wrapper function for calling functions in the parent package."""

    def __call__(self, *data: A, **star: R) -> A:
        raise NotImplementedError(self, data, star)


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


def wrapper(name: S) -> C[[Wrapper], A]:
    """"""

    def rapper(function: Wrapper) -> Wrapper:

        wrap = None

        def decorator(*data: A, **star: R) -> A:
            nonlocal wrap
            if not wrap:
                represent = repr(function)
                find = regex.match(
                    r"<function ([\w\.]+) ",
                    represent,
                )
                base = regex.match(
                    r"celestine\.package\.(.*)",
                    name,
                )
                wrap = load.find_function(base, find)

            try:
                result = function(*data, **star, wrap=wrap)
            except NotImplementedError:
                result = wrap(*data, **star)

            return result

        return decorator

    return rapper
