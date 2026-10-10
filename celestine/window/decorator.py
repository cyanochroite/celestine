""""""

from celestine.interface import (
    Element,
    Window,
)
from celestine.typed import (
    A,
    B,
    C,
    N,
    Protocol,
    R,
    S,
    ignore,
)

type Function = C[[Window, S], N]


class Call(Protocol):
    """Type for code functions."""

    def __call__(self, *data: A, **star: R) -> B:
        raise NotImplementedError(self, data, star)


class View(Protocol):
    """Type for view functions."""

    def __call__(self, element: Element) -> N:
        raise NotImplementedError(self, element)


def call(function: Call) -> Function:
    """"""

    def decorator(window: Window, name: S) -> N:
        window.code[name] = function

    return decorator


def view(function: View) -> Function:
    """"""

    def decorator(window: Window, name: S) -> N:
        _view(function, window, name)
        window.main = name

    return decorator


def _view(function: View, window: Window, name: S) -> N:
    views = window.drop(name)
    function(views)
    window.view[name] = views


ignore(call, view)
