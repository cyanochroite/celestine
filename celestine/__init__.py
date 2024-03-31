""""""

from celestine import (
    bank,
    load,
)
from celestine.data import (
    BLENDER,
    INTERFACE,
    REGISTER,
    UNREGISTER,
)
from celestine.session import begin_session
from celestine.typed import (
    LS,
    B,
    N,
    R,
)

bl_info = {
    "name": "celestine",
    "description": "A python framework for desktop applications.",
    "author": "mem_dixy",
    "version": (2023, 10, 7),
    "blender": (4, 0, 0),
    "location": "View3D > Properties > Object Properties > celestine",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "https://celestine.readthedocs.io/en/latest/",
    "tracker_url": "https://github.com/mem-dixy/celestine/",
    "category": "3D View",
}


def main(argument_list: LS, exit_on_error: B, **star: R) -> N:
    """Run the main program."""
    begin_session(argument_list, exit_on_error, **star)
    with bank.window:
        for name, function in bank.code.items():
            bank.window.code[name] = function

        for name, function in bank.view.items():
            view = bank.window.drop(name)
            function(view)
            bank.window.view[name] = view


def register() -> N:
    """
    Blender register function.

    This is a function which only runs when enabling the add-on,
    this means the module can be loaded without activating the add-on.
    """
    load.redirect(INTERFACE, BLENDER, REGISTER)


def unregister() -> N:
    """
    Blender unregister function.

    This is a function to unload anything setup by register,
    this is called when the add-on is disabled.
    """
    load.redirect(INTERFACE, BLENDER, UNREGISTER)
