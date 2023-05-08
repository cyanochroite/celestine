"""Run a bunch of auto formaters."""


import pyupgrade._main

from celestine.package.autoflake import main as autoflake
from celestine.package.black import main as black
from celestine.package.isort import main as isort
from celestine.package.pydocstringformatter import (
    main as pydocstringformatter,
)
from celestine.package.pyupgrade import main as pyupgrade


def clean(**star):
    """"""

    pyupgrade()

    pydocstringformatter()

    autoflake()

    isort()

    black()

    print("I am a talking cow.")
