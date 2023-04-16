""""""
import bpy  # pylint: disable=import-error

import celestine
from celestine.typed import (
    B,
    N,
)

from .package import (
    data,
    preferences,
)
from .window import Window

INTERFACE = "interface"
BLENDER = "blender"
PACKAGE = "package"
PREFERENCES = "preferences"


def image_format():
    """"""
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


def window(session, **star):
    """"""
    return Window(session, **star)


def main(call: B, **star) -> N:
    """Run the main program."""
    content = preferences.content()
    argument = f"-i blender {content.argument}"

    argv = argument.split()
    exit_on_error = False

    celestine.main(argv, exit_on_error, call=call, **star)


class celestine_click(bpy.types.Operator):
    """"""

    bl_label = "Mouse Click"
    bl_idname = "celestine.click"

    def execute(self, context):
        """"""
        mouse = (obj for obj in bpy.data.objects if obj.name == "mouse")
        mouse = next(mouse)

        x_dot = mouse.location.x
        y_dot = mouse.location.y
        main("poke", x_dot=x_dot, y_dot=y_dot)

        return {"FINISHED"}


class celestine_main(bpy.types.Panel):
    """"""

    bl_category = "celestine"
    bl_context = "object"
    bl_description = "Celestine Tab"
    bl_idname = "OBJECT_PT_celestine"
    bl_label = "Célestine"
    bl_options = {"HEADER_LAYOUT_EXPAND"}
    bl_order = 0
    bl_owner_id = ""
    bl_parent_id = ""
    bl_region_type = "WINDOW"
    bl_space_type = "PROPERTIES"
    bl_translation_context = "*"
    bl_ui_units_x = 0

    text = ""
    use_pin = False

    def draw(self, context):
        """"""

        content = preferences.content()
        self.layout.operator("celestine.click")
        if content.ready:
            self.layout.operator("celestine.start")
        else:
            self.layout.operator("celestine.finish")

    def draw_header(self, context):
        """"""

    def draw_header_preset(self, context):
        """"""


class celestine_start(bpy.types.Operator):
    """"""

    bl_description = "whati ti do"

    bl_label = "Startup"
    bl_idname = "celestine.start"

    def execute(self, _):
        """"""

        print("start")
        car = bpy.context.preferences.addons["celestine"].preferences
        data.start()
        preferences.start()
        car.ready = True

        main(None)

        return {"FINISHED"}


class celestine_finish(bpy.types.Operator):
    """"""

    bl_label = "Shutdown"
    bl_idname = "celestine.finish"

    def execute(self, _):
        """"""
        print("finish")
        preferences.finish()
        data.finish()
        return {"FINISHED"}


def register():
    """"""
    preferences.register()
    bpy.utils.register_class(celestine_start)
    bpy.utils.register_class(celestine_finish)
    bpy.utils.register_class(celestine_click)
    bpy.utils.register_class(celestine_main)


def unregister():
    """"""
    bpy.utils.unregister_class(celestine_main)
    bpy.utils.unregister_class(celestine_click)
    bpy.utils.unregister_class(celestine_finish)
    bpy.utils.unregister_class(celestine_start)
    preferences.unregister()
