""""""

from enum import Enum

from celestine.typed import (
    C,
    N,
)
from celestine.window.container import View


class State(Enum):
    """"""

    CODE = 1
    VIEW = 2


def main(function: C[[View], N]) -> C[[View], N]:
    def decorator(view1: View) -> N:
        function(view1)

    return decorator


def view(function: C[[View], N]) -> C[[View], N]:
    return function


CELESTINE = "celestine"
VERSION_NUMBER = "2023.10.7"
INTERFACE = "interface"
BLENDER = "blender"
REGISTER = "register"
UNREGISTER = "unregister"
