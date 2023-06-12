""""""

import pathlib

from . import AbstractPackage

try:
    import platformdirs

    appname = "celestine"
    appauthor = "celestine"
    version = "0.4"
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


class Package(AbstractPackage):
    """"""
