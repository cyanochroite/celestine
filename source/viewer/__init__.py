import os
import sys

import celestine

from viewer import main as module


bl_info = {
    "name": "Celestine - Image Viewer",
    "description": "Blnder stuff can do stuff wow cool.",
    "author": "Mem Dixy",
    "version": (0, 4, 0),
    "blender": (3, 0, 0),
    "location": "View 3D > Sidebar > Viewer",
    "warning": "Does not work. Work in progress. Not ready for publication.",
    "wiki_url": "https://mem-dixy.ch/",
    "tracker_url": "https://github.com/Mem-Dixy/Blender-Booru-Builder",
    "support": "COMMUNITY",
    "category": "3D View",
}


def register():
    """
    This is a function which only runs when enabling the add-on, this means the
    module can be loaded without activating the add-on.
    """
    path = sys.path[0]
    directory = os.path.dirname(path)
    argv = ["blender", "main"]
    main(directory, argv, False)


def unregister():
    """
    This is a function to unload anything setup by register, this is called
    when the add-on is disabled.
    """


def main(directory, argv, exit_on_error):
    """Run the main program."""
    window = [
        # module.main,
        module.zero,
        module.one,
        module.two,
    ]
    celestine.main(directory, argv, exit_on_error, window)
