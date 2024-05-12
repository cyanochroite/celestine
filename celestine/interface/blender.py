""""""

import bpy  # pylint: disable=import-error

import celestine
from celestine import bank
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
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
    LS,
    A,
    B,
    K,
    N,
    R,
    S,
    override,
)
from celestine.window.collection import (
    Area,
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
        (x_dot, y_dot) = self.area.world.centroid
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
    def make(self, canvas: A, **star: R) -> N:
        """"""
        super().make(canvas, **star)

        first = star.get("first")

        if first:
            return

        item = self.dictionary.get(self.name)
        self.hidden = item.hide_render

    def __init__(self, name: S, parent: K, **star: R) -> N:
        super().__init__(name, parent, **star)
        self.dictionary = bpy.data.objects


class Mouse(Abstract):
    """Should everyone get this?"""

    @override
    def make(self, canvas: A, **star: R) -> N:
        """"""
        if super().make(canvas, **star):
            diamond = Diamond()
            diamond.make(self.mesh)

            self.render()

    def __init__(self, mesh) -> N:
        self.mesh = mesh.soul
        self.text = "mouse"
        super().__init__("mouse", parent=None)
        self.keep = mesh


class Element(Element_, Abstract):
    """"""

    @override
    def make(self, canvas: A, **star: R) -> N:
        """"""
        if self.action or self.goto:
            data = f"button: {self.text}"
            self.keep = basic.text(self.name, self.canvas, data)
        elif self.text:
            self.keep = basic.text(self.name, self.canvas, self.text)
        else:
            # image
            image = data.image.load(self.path)
            material = UV.image(self.name, image)
            plane = basic.image(self.name, self.canvas, image.size)

            plane.body.data.materials.append(material)
            self.keep = plane

        self.render()
        super().make(canvas, **star)

    def update(self, image: S, **star: R) -> B:
        """"""
        super().update(image, **star)

        material = bpy.data.materials[self.name]
        node = material.node_tree.nodes["Image Texture"]
        node.image = data.image.load(image)

        return True


class View(View_, Abstract):
    """"""

    @override
    def make(self, canvas: A, **star: R) -> N:
        """"""
        if canvas:
            link = canvas.children.link
        else:
            link = bpy.context.scene.collection.children.link

        collection = data.collection(self.name)
        link(collection.soul)

        super().make(collection, **star)

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

    def __init__(self, name, element, **star: R) -> N:
        super().__init__(name, element, **star)
        self.dictionary = bpy.data.collections


class Window(Window_):
    """"""

    @override
    def make(self, **star: R) -> N:
        """"""
        first = self.call == "make"
        super().make(first=first, **star)

    @override
    def extension(self) -> LS:
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
    def turn(self, page: S, **star: R) -> N:
        """"""
        super().turn(page, **star)
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
        super().__exit__(exc_type, exc_value, traceback)

        if self.call == "make":
            return False

        page = bpy.context.scene.celestine.page
        self.page = self.view[page]

        call = getattr(self, self.call)
        call(**self.star)

        bank.dequeue()

        return False

    def __init__(self, *, call=None, **star: R) -> N:
        element = {
            "element": Element,
            "view": View,
            "window": self,
        }
        super().__init__(element, **star)
        self.area = Area.make(35, 20)

        self.dictionary = bpy.data.collections  # From View?

        self.frame = None
        self.mouse = None

        self.call = call
        self.star = star

        self.canvas = None
