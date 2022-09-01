# <pep8-80 compliant>
from blender import data
from blender import preferences


bl_info = {
    "name": "My Blender Plugin",
    "description": "Blnder stuff can do stuff wow cool.",
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
    This is a function which only runs when enabling the add-on, this means the
    module can be loaded without activating the add-on.
    """
    data.register()
    preferences.register()


def unregister():
    """
    This is a function to unload anything setup by register, this is called
    when the add-on is disabled.
    """
    preferences.unregister()
    data.unregister()
