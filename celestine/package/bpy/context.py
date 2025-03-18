""""""

from celestine.package.bpy.types import AddonPreferences
from celestine.typed import (
    D,
    N,
    S,
)


class Addon:
    """"""

    preferences: AddonPreferences


class preferences:
    """"""

    addons: D[S, Addon]

    def __init__(self) -> N:
        self.addons = {}
