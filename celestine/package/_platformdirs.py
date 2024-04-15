"""A package for determining appropriate platform-specific dirs."""

import os
import pathlib

from celestine.package._abstract import Abstract

try:
    import platformdirs

    appname = "celestine"
    appauthor = "celestine"
    version = None
    roaming = False
    multipath = False
    opinion = False
    ensure_exists = True

    directory = pathlib.Path(
        platformdirs.user_data_dir(
            appname,
            appauthor,
            version,
            roaming,
            ensure_exists,
        )
    )
except ModuleNotFoundError:
    import os

    directory = pathlib.Path(os.getcwd())


class Package(Abstract):
    """"""

    def __init__(self, name, pypi=None, **star):
        self.directory = pathlib.Path(os.getcwd())
