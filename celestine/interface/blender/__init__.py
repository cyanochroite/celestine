from .package import preferences
from .package import UV
from .package import mesh
from .package import data

import bpy  # pylint: disable=import-error
import bpy

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


# <pep8-80 compliant>


class celestine_click(bpy.types.Operator):
    bl_label = "Mouse Click"
    bl_idname = "celestine.click"

    def execute(self, context):
        print("start")
        mouse = next(obj for obj in bpy.data.objects if obj.name == "mouse")
        location = mouse.location
        x = round(location.x / 2.5) * 2.5
        y = round(location.y / 2.5) * 2.5
        z = 1
        mouse.location = (x, y, z)
        print("done")
        return {'FINISHED'}


class celestine_main(bpy.types.Panel):
    bl_category = "celestine"
    bl_context = ""
    bl_idname = "CELESTINE_PT_main"
    bl_label = "Main Panel"
    bl_options = {"HEADER_LAYOUT_EXPAND"}
    bl_order = 0
    bl_owner_id = ""
    bl_parent_id = ""
    bl_region_type = "UI"
    bl_space_type = "VIEW_3D"
    bl_translation_context = "*"
    bl_ui_units_x = 0

    def draw(self, _):
        content = preferences.content()
        if content.ready:
            self.layout.operator("celestine.unregister")
            self.layout.operator("celestine.click")
        else:
            self.layout.operator("celestine.register")


class celestine_register(bpy.types.Operator):
    bl_label = "Startup"
    bl_idname = "celestine.register"

    def execute(self, _):
        data.register()
        content = preferences.content()
        content.ready = True
        return {'FINISHED'}


class celestine_unregister(bpy.types.Operator):
    bl_label = "Shutdown"
    bl_idname = "celestine.unregister"

    def execute(self, _):
        content = preferences.content()
        content.ready = False
        data.unregister()
        return {'FINISHED'}


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
