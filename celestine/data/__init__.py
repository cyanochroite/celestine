""""""

import importlib

from celestine import (
    load,
    regex,
)
from celestine.interface import View
from celestine.typed import (
    A,
    B,
    C,
    M,
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


def wrap(*data: A, **star: R) -> A:
    """Builtins.KeyError: 'wrap' = You forgot '**star'."""
    function = star.pop("wrap")
    result = function(*data, **star)
    return result


def wrapper(name: S) -> C[[Wrapper], A]:
    """"""

    def rapper(function: Wrapper) -> Wrapper:
        represent = repr(function)

        def module() -> M:
            pattern = r"celestine\.package\.(.*)"
            if "abstract" in name:
                pattern += r"\.abstract"
            find = regex.match(pattern, name)
            result = importlib.import_module(find)
            return result

        def class_attribute() -> S:
            find = regex.match(
                r"<class '([\w\.]+)'>",
                represent,
            )
            length = len(name) + 1
            result = find[length:]
            return result

        def function_attribute() -> S:
            result = regex.match(
                r"<function ([\w\.]+) ",
                represent,
            )
            return result

        def attribute() -> S:
            result = ""
            if "class" in represent:
                result = class_attribute()
            if "function" in represent:
                result = function_attribute()
            return result

        _wrap = load.attribute(module(), attribute())

        def decorator(*data: A, **star: R) -> A:
            try:
                result = function(*data, **star, wrap=_wrap)
            except NotImplementedError:
                result = _wrap(*data, **star)
            except TypeError:
                #  Tried to call __init__
                result = _wrap(*data, **star)

            return result

        return decorator

    return rapper
