""""""

from celestine import load
from celestine.literal import (
    APPLICATION,
    BLENDER,
    INTERFACE,
    PACKAGE,
    REGISTER,
    UNREGISTER,
)
from celestine.typed import (
    LS,
    B,
    C,
    D,
    N,
    R,
    S,
)

bl_info = {
    "name": "celestine",
    "description": "A python framework for desktop applications.",
    "author": "mem_dixy",
    "version": (2023, 10, 7),
    "blender": (4, 1, 0),
    "location": "View3D > Properties > Object Properties > celestine",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "https://celestine.readthedocs.io/en/latest/",
    "tracker_url": "https://github.com/mem-dixy/celestine/",
    "category": "3D View",
}


def main(argument_list: LS, exit_on_error: B, **star: R) -> N:
    """Run the main program."""
    package = load.module(PACKAGE)
    for name in load.argument(PACKAGE):
        value = load.instance(PACKAGE, name, "Package")
        setattr(package, name, value)

    session = load.module("session")
    begin_session = getattr(session, "begin_session")
    window, application = begin_session(
        argument_list,
        exit_on_error,
        **star,
    )

    code: D[S, C] = {}
    view: D[S, C] = {}

    for module in load.modules(APPLICATION, application):
        code |= load.decorators(module, "code")
        view |= load.decorators(module, "scene")

    with window:
        for key, value in view.items():
            if "primary" in repr(value):
                window.main = key
                break
        else:
            window.main = next(iter(view))

        for name, function in code.items():
            window.code[name] = function

        for name, function in view.items():
            view = window.drop(name)
            function(view)
            window.view[name] = view


def register() -> N:
    """
    Blender register function.

    This is a function which only runs when enabling the add-on,
    this means the module can be loaded without activating the add-on.
    """
    load.instance(INTERFACE, BLENDER, REGISTER)


def unregister() -> N:
    """
    Blender unregister function.

    This is a function to unload anything setup by register,
    this is called when the add-on is disabled.
    """
    load.instance(INTERFACE, BLENDER, UNREGISTER)
