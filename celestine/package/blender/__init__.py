""""""

from celestine.package import Abstract
from celestine.typed import (
    N,
    R,
    S,
)


class Package(Abstract):
    """"""

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(name, pypi="bpy")
