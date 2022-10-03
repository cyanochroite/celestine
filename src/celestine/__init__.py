from celestine.session import load
from celestine.session import Session

BLENDER = "blender"

bl_info = {
    "name": "Celestine Image Viewer",
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
    load.module(BLENDER).register()


def unregister():
    """
    This is a function to unload anything setup by register, this is called
    when the add-on is disabled.
    """
    load.module(BLENDER).unregister()


def main(directory, argv, exit_on_error, application):
    """Run the main program."""
    session = Session(directory, argv, exit_on_error)
    with session.task.window(session) as window:
        for document in application:
            with window.page(document) as page:
                document(page)
