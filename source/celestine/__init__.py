from celestine.session import load
from celestine.session import Session

PACKAGE = "package"
BLENDER = "blender"
MAIN = "main"

bl_info = {
    "name": "Celestine",
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
    load.module(PACKAGE, BLENDER, MAIN).register()


def unregister():
    """
    This is a function to unload anything setup by register, this is called
    when the add-on is disabled.
    """
    load.module(PACKAGE, BLENDER, MAIN).unregister()


def zero(page):
    with page.line("head") as line:
        line.label("title", "Page 0")


def main(directory, argv, exit_on_error, application=zero):
    """Run the main program."""
    session = Session(directory, argv, exit_on_error)
    with session.task.window(session) as window:
        for document in application:
            window.page(document)
