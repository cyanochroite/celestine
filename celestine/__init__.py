""""""

from celestine import load
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
    "blender": (3, 3, 0),
    "location": "View3D > Properties > Object Properties > celestine",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "https://celestine.readthedocs.io/en/latest/",
    "tracker_url": "https://github.com/mem-dixy/celestine/",
    "category": "3D View",
}

def main(argument_list: LS, exit_on_error: B, **star: R) -> N:
    """Run the main program."""
    session = begin_session(argument_list, exit_on_error)

    window = session.interface.Window(session, **star)
    session.window = window

    with window:
        for name, function in session.code.items():
            window.code[name] = function

        for name, function in session.view.items():
            canvas = window.setup(name)
            container = window.drop(name, canvas=canvas)
            container.hide()
            function(container)
            window.view[name] = container

        window.page = window.view[session.main]
        window.page.show()




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


# Merge Code and View files. Mark Code functions. Scan all files in app.
# sys.meta_path.append(DebugFileLoader) # importer

# package name ref:
# Glue
# Bottle

# zipapp on pypi
# python -x importtime -c "filename"


# decorator   __call__


# split stream into load and save
