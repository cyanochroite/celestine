""""""

import os
import pathlib
import stat
import subprocess

from celestine.literal import (
    join,
)
from celestine.typed import (
    LS,
    N,
    P,
    Path,
    Z,
    ignore,
)


def process_open(path: P) -> N:
    """"""
    function = join("start", "file")
    os_start_file = getattr(os, function)
    os_start_file(path)


def process_run(*iterables: Path) -> N:
    """"""
    arguments: LS = []
    for iterable in iterables:
        item = str(iterable)
        arguments.append(item)
    # Using the "with" statement will block.
    subprocess.Popen(arguments)  # pylint: disable=consider-using-with


def process_wait(*iterables: Path) -> N:
    """"""
    arguments: LS = []
    for iterable in iterables:
        item = str(iterable)
        arguments.append(item)
    with subprocess.Popen(arguments) as process:
        process.wait()


def chown(top: P, permission: Z) -> N:
    """"""
    top.chmod(permission)
    for dirpath, dirnames, filenames in os.walk(top, True, None):
        for dirname in dirnames:
            path = pathlib.Path(dirpath, dirname)
            path.chmod(permission)
        for filename in filenames:
            path = pathlib.Path(dirpath, filename)
            path.chmod(permission)


def locked(folder: P) -> N:
    """"""
    chown(folder, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)


def unlock(folder: P) -> N:
    """"""
    chown(folder, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)


ignore(
    chown,
    locked,
    process_open,
    process_run,
    process_wait,
    unlock,
)
