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

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        for name, item in bpy.data.collections.items():
            if name == self.name:
                item.hide_render = True
                item.hide_viewport = True

    def render(self) -> N:
        """"""
        (x_dot, y_dot) = self.area.centroid.float
        # child sets mesh and then calls this
        self.keep.location = (x_dot, y_dot, 0)
        self.keep.rotation = (180, 0, 0)

    @override
    def show(self) -> N:
        """"""
        super().show()
        for name, item in bpy.data.collections.items():
            if name == self.name:
                item.hide_render = False
                item.hide_viewport = False


class Mouse(Abstract):
    """"""

    def __init__(self, hold: H, collection, mesh) -> N:
        self.mesh = mesh.soul
        self.text = "mouse"
        super().__init__(hold, collection, "mouse")
        self.keep = mesh

    def make(self) -> N:
        """"""

        diamond = Diamond()
        diamond.make(self.mesh)

        self.render()


class Button(Abstract, Button_):
    """"""

    def make(self) -> N:
        """"""

        width = len(self.data) / 4
        height = 1 / 20

        plane = quadrilateral.plane(self.canvas, self.data)
        plane.scale = (width, height, 1)

        text = basic.text(self.canvas, self.data, self.data)
        text.scale = (1 / width, 1 / height, 1)
        text.location = (-width / 4, -height, 0.1)

        text.parent = plane

        self.keep = plane
        self.render()


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

    def make(self) -> N:
        """"""

        image = data.image.load(self.path)
        material = UV.image(self.name, image)
        plane = basic.image(self.canvas, self.name, image.size)

        plane.body.data.materials.append(material)
        self.keep = plane
        self.render()

    def update(self, image: S, **star: R) -> B:
        """"""
        super().update(image, **star)

        material = bpy.data.materials[self.name]
        node = material.node_tree.nodes["Image Texture"]
        node.image = data.image.load(image)

        return True


class Label(Abstract, Label_):
    """"""

    def make(self) -> N:
        """"""
        self.keep = basic.text(self.canvas, self.data, self.data)
        self.render()


class View(Abstract, View_):
    """"""


class Window(Abstract, Window_):
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
    def setup(self, name):
        """"""
        # TODO REMOVE
        return data.collection.make(name)

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

        collection = data.collection.make("window")

        camera = data.camera.make(collection, "camera")
        camera.location = (+17.5, +10.0, -60.0)
        camera.rotation = (180, 0, 0)
        camera.ortho_scale = +35.0
        camera.type = "ORTHO"

        starlight = data.light.sun.make(collection, "light")
        starlight.rotation = (180, 0, 0)
        starlight.energy = 10.0
        starlight.diffuse_factor = 1.0
        starlight.specular_factor = 1.0
        starlight.volume_factor = 1.0
        starlight.angle = 0.0

        click = data.collection.make("click")
        click.soul.hide_select = False

        mesh = data.mesh.make(click, "mouse")
        mesh.location = (0, 0, -1)

        self.mouse = Mouse(self.hold, collection, mesh)
        self.mouse.make()

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
        if self.call == "make":
            super().__exit__(exc_type, exc_value, traceback)
            return False

        self.spot()

        page = bpy.context.scene.celestine.page
        self.page = self.view[page]

        item = self.view.get(page)
        item.show()

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
            "window": Window,
        }
        canvas = None
        super().__init__(hold, canvas, element, **star)
        self.area = Plane.make(20, 20)

        self.frame = None
        self.mouse = None

        self.call = call
        self.star = star
