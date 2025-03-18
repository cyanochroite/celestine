""""""

from typing import TypeAlias

from celestine.package.bpy.types import (
    AssetShelf,
    FileHandler,
    Header,
    KeyingSetInfo,
    Menu,
    Operator,
    Panel,
    RenderEngine,
    UIList,
)
from celestine.typed import (
    N,
    U,
)

Class: TypeAlias = U[
    AssetShelf,
    FileHandler,
    Header,
    KeyingSetInfo,
    Menu,
    Operator,
    Panel,
    RenderEngine,
    UIList,
]


def register_class(cls: Class) -> N:
    """"""


def unregister_class(cls: Class) -> N:
    """"""
