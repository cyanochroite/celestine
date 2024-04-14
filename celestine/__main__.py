""""""

import importlib
import os
import sys
from collections.abc import Sequence
from importlib.abc import MetaPathFinder
from importlib.machinery import ModuleSpec
from types import ModuleType
from typing import override


class CelestineMetaFinder(MetaPathFinder):
    """"""

    loader: importlib.abc.Loader

    @override
    def find_spec(
        self,
        fullname: str,
        # pylint: disable-next=unused-argument
        path: Sequence[str] | None,
        # pylint: disable-next=unused-argument
        target: ModuleType | None = None,
    ) -> ModuleSpec | None:
        """"""
        if fullname.startswith("celestine.package."):
            return ModuleSpec(fullname, self.loader)
        return None

    @override
    def __init__(self) -> None:
        package = importlib.import_module("celestine.package")
        self.loader = getattr(package, "Loader")()


sys.meta_path.insert(0, CelestineMetaFinder())
sys.path.insert(0, os.path.dirname(sys.path[0]))

celestine = importlib.import_module("celestine")
celestine.main(sys.argv[1:], True)
