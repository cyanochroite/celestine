""""""

from celestine.package import Abstract
from celestine.typed import (
    N,
    R,
)


class Package(Abstract):
    """"""

    def __init__(self, **star: R) -> N:
        super().__init__(pypi="bpy")
