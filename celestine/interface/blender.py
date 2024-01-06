""""""

import bpy  # pylint: disable=import-error

import celestine
from celestine import load
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
from celestine.package.blender.mesh import (
    basic,
    quadrilateral,
)
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
        Image.begin()
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
        Image.finish()
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


class Mouse(Abstract):
    """"""

    def __init__(self, hold: H, mesh) -> N:
        self.mesh = mesh.soul
        self.text = "mouse"
        super().__init__(hold, "mouse", parent=None)
        self.keep = mesh

    @override
    def make(self, canvas: A, **star: R) -> N:
        """"""
        first = star.get("first")

        if first:
            diamond = Diamond()
            diamond.make(self.mesh)

            self.render()
        else:
            item = bpy.data.objects.get(self.name)
            self.hidden = item.hide_render

        super().make(self.canvas, **star)


class Button(Abstract, Button_):
    """"""

    @override
    def make(self, canvas: A, **star: R) -> N:
        """"""
        first = star.get("first")

        if first:
            width = len(self.data) / 4
            height = 1 / 20

            plane = quadrilateral.plane(self.name, canvas)
            plane.scale = (width, height, 1)

            text = basic.text(self.data, canvas, self.data)
            text.scale = (1 / width, 1 / height, 1)
            text.location = (-width / 4, -height, 0.1)

            text.parent = plane

            self.keep = plane
            self.render()
        else:
            item = bpy.data.objects.get(self.name)
            self.hidden = item.hide_render

        super().make(self.canvas, **star)


class Image(Abstract, Image_):
    """"""

    default: data.image

    @classmethod
    def begin(cls):
        """"""
        name = "null.png"
        path = load.asset(name)
        cls.default = data.image.load(path)

    @classmethod
    def finish(cls):
        """"""
        item = cls.default
        data.image.remove(item)
        cls.default = None


    @override
    def make(self, canvas: A, **star: R) -> N:
        """"""
        first = star.get("first")

        if first:
            image = data.image.load(self.path)
            material = UV.image(self.name, image)
            plane = basic.image(self.name, canvas, image.size)

            plane.body.data.materials.append(material)
            self.keep = plane
            self.render()
        else:
            item = bpy.data.objects.get(self.name)
            self.hidden = item.hide_render

        super().make(self.canvas, **star)

        if not first:
            return


    def update(self, image: S, **star: R) -> B:
        """"""
        super().update(image, **star)

        material = bpy.data.materials[self.name]
        node = material.node_tree.nodes["Image Texture"]
        node.image = data.image.load(image)

        return True


class Label(Abstract, Label_):
    """"""

    @override
    def make(self, canvas: A, **star: R) -> N:
        """"""
        first = star.get("first")

        if first:
            self.keep = basic.text(self.name, canvas, self.data)
            self.render()
        else:
            item = bpy.data.objects.get(self.name)
            self.hidden = item.hide_render

        super().make(self.canvas, **star)


class View(View_):
    """"""

    @override
    def make(self, canvas: A, **star: R) -> N:
        """"""
        first = star.get("first")
        if first:
            self.canvas = data.collection(self.name)
            if not canvas:
                bpy.context.scene.collection.children.link(self.canvas.soul)
            else:
                canvas.children.link(self.canvas.soul)
        else:
            item = bpy.data.collections.get(self.name)
            self.hidden = item.hide_render

        super().make(self.canvas, **star)

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


class Window(Window_):
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

        self.mouse = Mouse(self.hold, mesh)
        self.mouse.make(collection, first=True)

        @classmethod
        def bind(cls, collection, name, soul):
            """Give an existing soul a body."""
            body = bpy.data.objects.new(name, soul)
            collection.objects.link(body)
            return cls(body, soul)

        override = context()
        bpy.ops.view3d.toggle_shading(override, type="RENDERED")

        if self.call == "make":
            bpy.ops.view3d.view_camera(override)

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

            self.turn(self.hold.main)

            return False

        self.make(None, first=False)

        page = bpy.context.scene.celestine.page
        self.page = self.view[page]

        call = getattr(self, self.call)
        call(**self.star)

        self.hold.dequeue()

        return False

    @override
    def __init__(self, hold: H, *, call=None, **star: R) -> N:
        element = {
            "button": Button,
            "image": Image,
            "label": Label,
            "view": View,
            "window": self,
        }
        super().__init__(hold, element, **star)
        self.area = Plane.make(20, 20)

        self.frame = None
        self.mouse = None

        self.call = call
        self.star = star
