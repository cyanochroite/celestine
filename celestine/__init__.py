""""""

import importlib
import importlib.abc
import importlib.machinery
import sys
from importlib.abc import MetaPathFinder
from importlib.machinery import ModuleSpec

from celestine import bank
from celestine.session import begin_session
from celestine.typed import (
    LS,
    MS,
    OM,
    SS,
    B,
    M,
    N,
    R,
    S,
    ignore,
    override,
)
from celestine.unicode import FULL_STOP
from celestine.loader import loader


def main(argument_list: LS, exit_on_error: B, **star: R) -> N:
    """Run the main program."""
    loader()
    begin_session(argument_list, exit_on_error, **star)

    with bank.window:
        for name, function in bank.code.items():
            bank.window.code[name] = function

        for name, function in bank.view.items():
            view = bank.window.drop(name)
            function(view)
            bank.window.view[name] = view
