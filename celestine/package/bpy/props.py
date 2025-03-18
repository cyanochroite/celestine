""""""

from celestine.package.bpy.types import (
    ID,
    PropertyGroup,
)
from celestine.typed import (
    NR,
    TD,
    UN,
    B,
    N,
    S,
    Z,
)


class _Bool(TD):
    """"""

    default: B
    description: S
    name: S


class _Pointer(TD):
    """"""

    type: ID | PropertyGroup


class _String(TD):
    """"""

    default: NR[S]
    description: S
    maxlen: NR[Z]
    name: S
    subtype: NR[S]


class BoolProperty:
    """"""

    def __init__(self, **star: UN[_Bool]) -> N:
        """"""
        raise NotImplementedError(self, star)


class StringProperty:
    """"""

    def __init__(self, **star: UN[_String]) -> N:
        """"""
        raise NotImplementedError(self, star)
