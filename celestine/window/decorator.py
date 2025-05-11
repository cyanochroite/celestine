""""""

from celestine.interface import (
    View,
    Window,
)
from celestine.typed import (
    ANY,
    B,
    C,
    N,
    Protocol,
    R,
    S,
)

type Function = C[[Window, S], N]


class Call(Protocol):
    """Type for code functions."""

    def __call__(self, *data: ANY, **star: R) -> B:
        raise NotImplementedError(self, data, star)


class Draw(Protocol):
    """Type for draw functions."""

    def __call__(self, view: View) -> N:
        raise NotImplementedError(self, view)


def call(function: Call) -> Function:
    """"""

    def decorator(window: Window, name: S) -> N:
        window.code[name] = function

    return decorator


def draw(function: Draw) -> Function:
    """"""

    def decorator(window: Window, name: S) -> N:
        _view(function, window, name)
        if not window.main or "main" in name:
            window.main = name

    return decorator


def main(function: Draw) -> Function:
    """"""

    def decorator(window: Window, name: S) -> N:
        _view(function, window, name)
        window.main = name

    return decorator


def _view(function: Draw, window: Window, name: S) -> N:
    view = window.drop(name)
    function(view)
    window.view[name] = view
