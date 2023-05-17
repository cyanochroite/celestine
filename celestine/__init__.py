""""""

from celestine import load
from celestine.session.parsering import start_session
from celestine.typed import (
    B,
    L,
    N,
    S,
)

INTERFACE = "interface"
BLENDER = "blender"
APPLICATION = "application"

bl_info = {
    "name": "Célestine (Framework)",
    "description": "A python framework for desktop applications.",
    "author": "mem_dixy",
    "version": (0, 4, 0),
    "blender": (3, 3, 0),
    "location": "View3D > Properties > Object Properties > Celestine",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "https://celestine.readthedocs.io/en/latest/",
    "tracker_url": "https://github.com/mem-dixy/celestine/",
    "category": "3D View",
}


def main(argument_list: L[S], exit_on_error: B, **star) -> N:
    """Run the main program."""

    session = start_session(argument_list, exit_on_error)
    with session.interface.window(session, **star) as window:
        for name, document in session.call.items():
            window.task.set(name, document)

        for name, document in session.view.items():
            window.view(name, document)


def register() -> N:
    """
    Blender register function.

    This is a function which only runs when enabling the add-on,
    this means the module can be loaded without activating the add-on.
    """
    blender = load.module(INTERFACE, BLENDER)
    blender.register()


def unregister() -> N:
    """
    Blender unregister function.

    This is a function to unload anything setup by register,
    this is called when the add-on is disabled.
    """
    blender = load.module(INTERFACE, BLENDER)
    blender.unregister()
