""""""

# <pep8-80 compliant>
import bpy  # pylint: disable=import-error

CELESTINE = "celestine"


def content():
    """"""
    return bpy.context.preferences.addons[CELESTINE].preferences


class CelestineAddonPreferences(bpy.types.AddonPreferences):
    """"""

    bl_idname = CELESTINE

    argument: bpy.props.StringProperty(
        name="Command Line Arguments",
        description="Interface already accounted for.",
        default="-a demo main -l en",
        maxlen=256,
    )

    root: bpy.props.StringProperty(
        name="Root Image Folder",
        description="Location of your image collection.",
        subtype="DIR_PATH",
    )

    filepath: bpy.props.StringProperty(
        name="Example File Path",
        description="Location of your image collection.",
        subtype="FILE_PATH",
    )

    ready: bpy.props.BoolProperty(
        name="Application Ready",
        description="Tells the program everything is set up and ready.",
        default=False,
    )

    password: bpy.props.StringProperty(
        name="Password",
        default="",
        options={"HIDDEN", "SKIP_SAVE"},
        subtype="PASSWORD",
    )

    def draw(self, context):
        """"""
        layout = self.layout
        layout.prop(self, "argument")
        # unused
        layout.label(text="This is a preferences view for our add-on.")
        layout.prop(self, "root")
        layout.prop(self, "filepath")
        layout.prop(self, "ready")
        layout.prop(self, "password")


class CelestinePropertyGroup(bpy.types.PropertyGroup):
    """"""
    page: bpy.props.StringProperty(
        name="Page",
        description="Which page of the book to show.",
        default="main",
    )


def register():
    """"""
    bpy.utils.register_class(CelestineAddonPreferences)
    bpy.utils.register_class(CelestinePropertyGroup)
    bpy.types.Scene.celestine = bpy.props.PointerProperty(
        type=CelestinePropertyGroup
    )


def unregister():
    """"""
    bpy.utils.unregister_class(CelestinePropertyGroup)
    bpy.utils.unregister_class(CelestineAddonPreferences)


def start():
    """"""
    state = content()
    state.ready = True


def finish():
    """"""
    state = content()
    state.ready = False
