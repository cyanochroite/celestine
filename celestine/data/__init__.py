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
    J,
    N,
    Protocol,
    R,
    S,
    J,
)


class Code(Protocol):
    """Type for code functions."""

    def __call__(self, **star: R) -> B:
        raise NotImplementedError(self, star)


class Draw(Protocol):
    """Type for draw functions."""

    def __call__(self, view: View) -> N:
        raise NotImplementedError(self, view)


class Stub(Protocol):
    """Type for code functions."""

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


def stub(name: S) -> C[[Stub], Stub]:
    """"""

    def wrapper(function: Stub) -> Stub:

        cache = None

        def decorator(*data: A, **star: R) -> A:
            nonlocal cache
            if not cache:
                pattern = r"<function ([\w\.]+) "
                string = repr(function)
                find = regex.match(pattern, string)

                split = name.split(FULL_STOP)
                index = split[-1]
                source = bank.package[index].package
                cache = load.find_function(source, find)

            try:
                result = function(*data, **star)
            except NotImplementedError:
                result = cache(*data, **star)

            return result

        return decorator

    return wrapper
