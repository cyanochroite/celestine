""""""

import bpy  # pylint: disable=import-error

from celestine import bank
import celestine
from celestine.interface import Abstract as Abstract_
from celestine.interface import Button as Button_
from celestine.interface import Image as Image_
from celestine.interface import Label as Label_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.package.blender import (
    UV,
    data,
    preferences,
)
from celestine.package.blender.data.collection import _collection
from celestine.package.blender.mesh import basic
from celestine.package.blender.mesh.quadrilateral import Diamond
from celestine.typed import (
    A,
    B,
    H,
    N,
    R,
    S,
    override,
)
from celestine.window.collection import (
    Plane,
    Point,
)

COLLECTION = _collection


INTERFACE = "interface"
BLENDER = "blender"
PACKAGE = "package"
PREFERENCES = "preferences"


def main(call: B, **star: R) -> N:
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
        point = Point(x_dot, y_dot)
        main("click", point=point)

        return {"FINISHED"}


class celestine_main(bpy.types.Panel):
    """"""

    bl_category = "celestine"
    bl_context = "object"
    bl_description = "Celestine Tab"
    bl_idname = "OBJECT_PT_celestine"
    bl_label = "celestine"
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
            self.layout.operator("celestine.begin")
        else:
            self.layout.operator("celestine.finish")

    def draw_header(self, context):
        """"""

    def draw_header_preset(self, context):
        """"""


class celestine_begin(bpy.types.Operator):
    """"""

    bl_description = "whati ti do"

    bl_label = "Startup"
    bl_idname = "celestine.begin"

    def execute(self, _):
        """"""

        print("begin")
        car = bpy.context.preferences.addons["celestine"].preferences
        data.begin()
        preferences.begin()
        car.ready = True

        main("make")

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
    bpy.utils.register_class(celestine_begin)
    bpy.utils.register_class(celestine_finish)
    bpy.utils.register_class(celestine_click)
    bpy.utils.register_class(celestine_main)


def unregister():
    """"""
    bpy.utils.unregister_class(celestine_main)
    bpy.utils.unregister_class(celestine_click)
    bpy.utils.unregister_class(celestine_finish)
    bpy.utils.unregister_class(celestine_begin)
    preferences.unregister()


#########


def context():
    """"""
    for area in bpy.context.screen.areas:
        if area.type == "VIEW_3D":
            override = bpy.context.copy()
            override["area"] = area
            return override
    return None


class Abstract(Abstract_):
    """"""

    def render(self) -> N:
        """"""
        (x_dot, y_dot) = self.area.centroid.float
        # child sets mesh and then calls this
        self.keep.location = (x_dot, y_dot, 0)
        self.keep.rotation = (180, 0, 0)

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        item = bpy.data.objects.get(self.name)
        if item:
            item.hide_render = True
            item.hide_viewport = True

    @override
    def show(self) -> N:
        """"""
        super().show()
        item = bpy.data.objects.get(self.name)
        if item:
            item.hide_render = False
            item.hide_viewport = False

    @override
    def make(self, canvas: A, **star: R) -> B:
        """"""
        super().make(canvas, **star)

        first = star.get("first")

        if first:
            return True

        item = self.dictionary.get(self.name)
        self.hidden = item.hide_render
        return False

    def __init__(self, hold: H, name: S, **star: R) -> N:
        super().__init__(hold, name, **star)
        self.dictionary = bpy.data.objects


class Mouse(Abstract):
    """Should everyone get this?"""

    def __init__(self, hold: H, mesh) -> N:
        self.mesh = mesh.soul
        self.text = "mouse"
        super().__init__(hold, "mouse", parent=None)
        self.keep = mesh

    @override
    def make(self, canvas: A, **star: R) -> B:
        """"""
        if super().make(canvas, **star):
            diamond = Diamond()
            diamond.make(self.mesh)

            self.render()
        return True


class Button(Button_, Abstract):
    """"""

    @override
    def make(self, canvas: A, **star: R) -> B:
        """"""
        if super().make(canvas, **star):
            data = f"button: {self.data}"
            self.keep = basic.text(self.name, self.canvas, data)
            self.render()
        return True


class Image(Image_, Abstract):
    """"""

    @override
    def make(self, canvas: A, **star: R) -> B:
        """"""
        if super().make(canvas, **star):
            image = data.image.load(self.path)
            material = UV.image(self.name, image)
            plane = basic.image(self.name, self.canvas, image.size)

            plane.body.data.materials.append(material)
            self.keep = plane
            self.render()

        return True

    def update(self, image: S, **star: R) -> B:
        """"""
        super().update(image, **star)

        material = bpy.data.materials[self.name]
        node = material.node_tree.nodes["Image Texture"]
        node.image = data.image.load(image)

        return True


class Label(Label_, Abstract):
    """"""

    @override
    def make(self, canvas: A, **star: R) -> B:
        """"""
        if super().make(canvas, **star):
            self.keep = basic.text(self.name, self.canvas, self.data)
            self.render()

        return True


class View(View_, Abstract):
    """"""

    @override
    def make(self, canvas: A, **star: R) -> B:
        """"""
        if canvas:
            link = canvas.children.link
        else:
            link = bpy.context.scene.collection.children.link

        collection = data.collection(self.name)
        link(collection.soul)

        super().make(collection, **star)

        return True

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        item = bpy.data.collections.get(self.name)
        if item:
            item.hide_render = True
            item.hide_viewport = True

    @override
    def show(self) -> N:
        """"""
        super().show()
        item = bpy.data.collections.get(self.name)
        if item:
            item.hide_render = False
            item.hide_viewport = False

    def __init__(self, hold, name, element, **star: R) -> N:
        super().__init__(hold, name, element, **star)
        self.dictionary = bpy.data.collections


class Window(Window_, Abstract):
    """"""

    @override
    def extension(self):
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

    @override
    def turn(self, page):
        """"""
        super().turn(page)
        bpy.context.scene.celestine.page = page

    @override
    def __enter__(self):
        if self.call is None:
            print("THIS IS BEST RUN AS A BLENDER ADD-ONS")
            register()
            data.begin()
        elif self.call != "make":
            return self

        super().__enter__()

        for camera in bpy.data.cameras:
            data.camera.remove(camera)
        for collection in bpy.data.collections:
            data.collection.remove(collection)
        for curve in bpy.data.curves:
            data.curve.remove(curve)
        for image in bpy.data.images:
            data.image.remove(image)
        for light in bpy.data.lights:
            data.light.remove(light)
        for material in bpy.data.materials:
            data.material.remove(material)
        for mesh in bpy.data.meshes:
            data.mesh.remove(mesh)
        for texture in bpy.data.textures:
            data.texture.remove(texture)

        collection = data.collection("window")
        bpy.context.scene.collection.children.link(collection.soul)

        camera = data.camera("camera", collection)
        camera.location = (+17.5, +10.0, -60.0)
        camera.rotation = (180, 0, 0)
        camera.ortho_scale = +35.0
        camera.type = "ORTHO"

        starlight = data.light.sun("light", collection)
        starlight.rotation = (180, 0, 0)
        starlight.energy = 10.0
        starlight.diffuse_factor = 1.0
        starlight.specular_factor = 1.0
        starlight.volume_factor = 1.0
        starlight.angle = 0.0

        click = data.collection("click")
        bpy.context.scene.collection.children.link(click.soul)
        click.soul.hide_select = False

        mesh = data.mesh("mouse", click)
        mesh.location = (0, 0, -1)

        self.mouse = Mouse(mesh)
        self.mouse.make(collection, first=True)

        @classmethod
        def bind(cls, collection, name, soul):
            """Give an existing soul a body."""
            body = bpy.data.objects.new(name, soul)
            collection.objects.link(body)
            return cls(body, soul)

        for area in bpy.context.screen.areas:
            if area.type == "VIEW_3D":
                for space in area.spaces:
                    if space.type == "VIEW_3D":
                        space.shading.type = "RENDERED"

        for window in bpy.context.window_manager.windows:
            screen = window.screen
            for area in screen.areas:
                if area.type == "VIEW_3D":
                    for region in area.regions:
                        if region.type == "WINDOW":
                            temp_override = bpy.context.copy()
                            temp_override["window"] = window
                            temp_override["screen"] = screen
                            temp_override["area"] = area
                            temp_override["region"] = region
                            space = area.spaces[0]

        if self.call == "make":
            with bpy.context.temp_override(**temp_override):
                bpy.ops.view3d.view_camera()

        return self

    @override
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            raise exc_type
        if exc_value:
            raise exc_value
        if traceback:
            raise traceback

        self.spot(self.area)

        if self.call == "make":
            self.make(None, first=True)

            for _, item in self:
                item.hide()

            self.turn(bank.main)

            return False

        self.make(None, first=False)

        page = bpy.context.scene.celestine.page
        self.page = self.view[page]

        call = getattr(self, self.call)
        call(**self.star)

        bank.dequeue()

        return False

    @override
    def __init__(self, *, call=None, **star: R) -> N:
        element = {
            "button": Button,
            "image": Image,
            "label": Label,
            "view": View,
            "window": self,
        }
        super().__init__(element, **star)
        self.dictionary = bpy.data.collections  # From View?

        self.area = Plane.make(20, 20)

        self.frame = None
        self.mouse = None

        self.call = call
        self.star = star
