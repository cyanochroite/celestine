""""""

from celestine.package import Abstract
from celestine.typed import R


class Package(Abstract):
    """"""

    def __init__(self, hold, /, name, **star: R):
        super().__init__(hold, name, pypi="bpy")
