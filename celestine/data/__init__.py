""""""

from enum import Enum

from celestine.typed import (
    C,
    N,
    H,
    R,
)
from celestine.window.container import View


class State(Enum):
    """"""

    CODE = 1
    VIEW = 2


def main(function: C[[View], N]) -> C[[View], N]:
    def decorator(view: View) -> N:
        function(view)

    return decorator


def scene(function: C[[View], N]) -> C[[View], N]:
    def decorator(view: View) -> N:
        function(view)

    return decorator


def code(function: C[[View], N]) -> C[[View], N]:
    def decorator(hold: H, **star: R) -> N:
        function(hold, **star)

    return decorator


CELESTINE = "celestine"
VERSION_NUMBER = "2023.10.7"
INTERFACE = "interface"
BLENDER = "blender"
REGISTER = "register"
UNREGISTER = "unregister"


def clamp(minimum, midterm, maximum):
    """The order of the inputs actually don't matter."""
    return sorted((minimum, midterm, maximum))[1]
