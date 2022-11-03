import sys

bl_info = {
    "name": "Celestine - Image Viewer",
    "description": "Blnder stuff can do stuff wow cool.",
    "author": "mem_dixy",
    "version": (0, 4, 0),
    "blender": (3, 0, 0),
    "location": "View 3D > Sidebar > Viewer",
    "warning": "Does not work. Work in progress. Not ready for publication.",
    "wiki_url": "https://celestine.readthedocs.io/en/latest/",
    "tracker_url": "https://github.com/mem-dixy/celestine/",
    "support": "COMMUNITY",
    "category": "3D View",
}


def register():
    """
    This is a function which only runs when enabling the add-on, this means the
    module can be loaded without activating the add-on.
    """
    main(sys.path[0], ["blender", "main"], False)


def unregister():
    """
    This is a function to unload anything setup by register, this is called
    when the add-on is disabled.
    """


def module(*paths):
    """Load an internal module from anywhere in the application."""
    iterable = ["viewer", *paths]
    name = ".".join(iterable)
    file = __import__(name)
    for _path in paths:
        file = getattr(file, _path)
    return file


def main(directory, argv, exit_on_error):
    """Run the main program."""
    celestine = __import__("celestine")
    window = module("window")

    application = [
        # module.main,
        window.zero,
        window.one,
        window.two,
    ]
    celestine.main(directory, argv, exit_on_error, application)
