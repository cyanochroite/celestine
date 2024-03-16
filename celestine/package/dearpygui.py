"""DearPyGui: A simple Python GUI Toolkit."""


from celestine.typed import (
    H,
    R,
    N,
    S,
)

from . import Abstract


class Package(Abstract):
    """"""

    def tag_root(self, tag: S) -> S:
        """"""
        root = tag.split("_")[0]
        combine = f"{root}"
        return combine

    def __init__(self, hold: H, name: S, **star: R) -> N:
        super().__init__(hold, name, pypi="dearpygui.dearpygui")
