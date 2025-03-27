"""A package for determining appropriate platform-specific dirs."""

from celestine.package import Abstract
from celestine.typed import (
    B,
    N,
    R,
    S,
    ignore,
)


class Package(Abstract):
    """"""


def user_data_dir(
    appname: S,
    appauthor: B,
    version: N,
    roaming: B,
    ensure_exists: B,
    **star: R,
) -> S:
    """"""
    ignore(star)
    raise NotImplementedError(
        appname, appauthor, version, roaming, ensure_exists
    )


ignore(Package, user_data_dir)
