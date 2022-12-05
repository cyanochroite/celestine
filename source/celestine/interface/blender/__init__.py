from .window import Window


def image_format():
    return [
        ".bmp",
        ".sgi",
        ".rgb",
        ".bw",
        ".png",
        ".jpg",
        ".jpeg",
        ".jp2",
        ".j2c",
        ".tga",
        ".cin",
        ".dpx",
        ".exr",
        ".hdr",
        ".tif",
        ".tiff",
        ".webp",
    ]


def window(session):
    return Window(session)


def register():
    bpy.utils.register_class(celestine_unregister)
    preferences.register()
    bpy.utils.register_class(celestine_main)
    bpy.utils.register_class(celestine_click)
    bpy.utils.register_class(celestine_register)


def unregister():
    bpy.utils.unregister_class(celestine_register)
    bpy.utils.unregister_class(celestine_click)
    bpy.utils.unregister_class(celestine_main)
    preferences.unregister()
    bpy.utils.unregister_class(celestine_unregister)
