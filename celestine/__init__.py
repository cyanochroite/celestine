""""""

from celestine import load

from celestine.session.parser import start_session

from celestine.text import CELESTINE
from celestine.text.directory import BLENDER


from celestine.text.directory import INTERFACE


bl_info = {
    "name": "celestine",
    "description": "The Celestine Image Viewer.",
    "author": "mem_dixy",
    "version": (0, 4, 0),
    "blender": (3, 3, 0),
    "location": "View 3D > Sidebar > Viewer",
    "wiki_url": "https://celestine.readthedocs.io/en/latest/",
    "tracker_url": "https://github.com/mem-dixy/celestine/",
    "support": "COMMUNITY",
    "category": "3D View",
}


def register() -> None:
    """
    This is a function which only runs when enabling the add-on, this
    means the module can be loaded without activating the add-on.
    """
    load.module(INTERFACE, BLENDER).register()
    # main([BLENDER], False)


def unregister() -> None:
    """
    This is a function to unload anything setup by register, this is
    called when the add-on is disabled.
    """
    load.module(INTERFACE, BLENDER).unregister()


def main(argv: list[str], exit_on_error: bool) -> None:
    """Run the main program."""
    session = start_session(argv, exit_on_error)
    with session.interface.window(session) as window:
        function = load.function(session.application)
        for (name, document) in function.items():
            window.page(name, document)
