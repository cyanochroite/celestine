""""""

from celestine import load
from celestine.load import function
from celestine.session.parser import start_session

INTERFACE = "interface"
BLENDER = "blender"
PACKAGE = "package"
PREFERENCES = "preferences"


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


def register() -> None:
    """
    This is a function which only runs when enabling the add-on,
    this means the module can be loaded without activating the add-on.
    """
    load.module(INTERFACE, BLENDER).register()


def unregister() -> None:
    """
    This is a function to unload anything setup by register,
    this is called when the add-on is disabled.
    """
    load.module(INTERFACE, BLENDER).unregister()


def main(argv: list[str], exit_on_error: bool) -> None:
    """Run the main program."""
    session = start_session(argv, exit_on_error)
    with session.interface.window(session) as window:
        call = function.load(session.call)
        for name, document in call.items():
            window.task.set(name, document)

        view = function.load(session.view)
        for name, document in view.items():
            window.page(name, document)


def blender1():
    """Run the main program."""
    preferences = load.module(INTERFACE, BLENDER, PACKAGE, PREFERENCES)
    content = preferences.content()
    argument = f"-i blender {content.argument}"
    argv = argument.split()
    exit_on_error = False

    session = start_session(argv, exit_on_error)
    with session.interface.window(session) as window:
        function1 = load.function(session.application)
        for name, document in function1.items():
            window.page(name, document)


def blender2(task="draw", **kwargs):
    """Run the main program."""
    preferences = load.module(INTERFACE, BLENDER, PACKAGE, PREFERENCES)
    content = preferences.content()
    argument = f"-i blender {content.argument}"
    argv = argument.split()
    exit_on_error = False

    session = start_session(argv, exit_on_error)
    window = session.interface.window(session)

    function1 = load.function(session.application)
    for name, document in function1.items():
        window.page(name, document)

    call = getattr(window, task)
    call(**kwargs)
