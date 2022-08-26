"""Package blender."""


def argument(argument):
    """Build up the argument."""
    return argument


def attribute():
    """Build up the attribute file."""
    return ()


def default():
    """Build up the default file."""
    return ()

"""
An add-on is simply a Python module with some additional requirements so
Blender can display it in a list with useful information.
"""
# <pep8-80 compliant>
from . import main
from . import preferences


bl_info = {
    "name": "Blender Booru Builder",
    "description": "Add, tag, and browse images on your computer.",
    "author": "Mem Dixy",
    "version": (0, 0, 4),
    "blender": (2, 91, 0),
    "location": "View 3D > Sidebar > Viewer",
    "warning": "Does not work. Work in progress. Not ready for publication.",
    "wiki_url": "https://mem-dixy.ch/",
    "tracker_url": "https://github.com/Mem-Dixy/Blender-Booru-Builder",
    "support": "COMMUNITY",
    "category": "3D View",
}


def register():
    """
    This is a function which only runs when enabling the add-on,
    this means the module can be loaded without activating the add-on.
    """
    main.register()
    preferences.register()


def unregister():
    """
    This is a function to unload anything setup by register,
    this is called when the add-on is disabled.
    """
    preferences.unregister()
    main.unregister()
