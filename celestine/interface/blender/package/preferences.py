# <pep8-80 compliant>
import bpy  # pylint: disable=import-error

CELESTINE = "celestine"


def content():
    return bpy.context.preferences.addons[CELESTINE].preferences


class CelestineAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = CELESTINE

    root: bpy.props.StringProperty(
        name="Root Image Folder",
        description="Location of your image collection.",
        subtype='DIR_PATH'
    )

    filepath: bpy.props.StringProperty(
        name="Example File Path",
        description="Location of your image collection.",
        subtype='FILE_PATH',
    )

    number: bpy.props.IntProperty(
        name="Example Number",
        description="Location of your image collection.",
        default=4
    )

    change: bpy.props.IntProperty(
        name="Prove this worked",
        description="Location of you.",
        default=4
    )

    boolean: bpy.props.BoolProperty(
        name="Example Boolean",
        description="Location of your image collection.",
        default=False
    )

    ready: bpy.props.BoolProperty(
        name="Application Ready",
        description="Tells the program everything is set up and go to go.",
        default=False
    )

    blender_id_password: bpy.props.StringProperty(
        name='Password',
        default='',
        options={'HIDDEN', 'SKIP_SAVE'},
        subtype='PASSWORD'
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="This is a preferences view for our add-on")
        layout.prop(self, "root")
        # unused
        layout.prop(self, "filepath")
        layout.prop(self, "change")
        layout.prop(self, "number")
        layout.prop(self, "ready")
        layout.prop(self, "boolean")


def register():
    bpy.utils.register_class(CelestineAddonPreferences)


def unregister():
    bpy.utils.unregister_class(CelestineAddonPreferences)
