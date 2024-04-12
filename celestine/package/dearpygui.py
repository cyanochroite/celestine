"""DearPyGui: A simple Python GUI Toolkit."""


from celestine.session import Abstract
from celestine.typed import (
    N,
    R,
    S,
)


class Package(Abstract):
    """"""

    def tag_root(self, tag: S) -> S:
        """"""
        root = tag.split("_")[0]
        combine = f"{root}"
        return combine

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(name, pypi="dearpygui.dearpygui")
