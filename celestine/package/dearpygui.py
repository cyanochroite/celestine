""""DearPyGui: A simple Python GUI Toolkit."""


from celestine.typed import (
    R,
    S,
)

from . import Abstract


class Package(Abstract):
    """"""

    def tag_root(self, tag):
        """"""
        root = tag.split("_")[0]
        combine = f"{root}"
        return combine

    def __init__(self, hold: R, name: S, **star):
        super().__init__(hold, name, pypi="dearpygui.dearpygui")
