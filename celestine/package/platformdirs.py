"""A package for determining appropriate platform-specific dirs."""

import pathlib

from celestine.package import Abstract
from celestine.typed import P

directory: P


class Package(Abstract):
    """"""

    @property
    def directory(self) -> P:
        """"""
        user_data_dir = getattr(self.package, "user_data_dir")
        path = user_data_dir(
            appname="celestine",
            appauthor=False,
            version=None,
            roaming=False,
            ensure_exists=True,
        )
        result = pathlib.Path(path)
        return result
