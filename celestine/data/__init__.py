""""""

from enum import Enum

from celestine.typed import (
    B,
    C,
    N,
)
from celestine.window.container import View


class State(Enum):
    """"""

    CODE = 1
    VIEW = 2


def main(function) -> C[[View], N]:
    def decorator(view: View) -> B:
        function(view)
        return True

    return decorator


CELESTINE = "celestine"
VERSION_NUMBER = "2023.10.7"
INTERFACE = "interface"
BLENDER = "blender"
REGISTER = "register"
UNREGISTER = "unregister"
