""""""

from celestine import load
from celestine.data import (
    BLENDER,
    INTERFACE,
    REGISTER,
    UNREGISTER,
)
from celestine.session import start_session
from celestine.typed import (
    B,
    L,
    N,
    S,
)

bl_info = {
    "name": "celestine",
    "description": "A python framework for desktop applications.",
    "author": "mem_dixy",
    "version": (0, 4, 0),
    "blender": (3, 3, 0),
    "location": "View3D > Properties > Object Properties > celestine",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "https://celestine.readthedocs.io/en/latest/",
    "tracker_url": "https://github.com/mem-dixy/celestine/",
    "category": "3D View",
}


def main(argument_list: L[S], exit_on_error: B, **star) -> N:
    """Run the main program."""

    session = start_session(argument_list, exit_on_error)
    window = session.interface.window(session, **star)
    session.window = window

    with window:
        for name, function in session.code.items():
            window.code(name, function)

        for name, function in session.view.items():
            window.view(name, function)


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
