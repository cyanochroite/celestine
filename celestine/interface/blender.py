""""""

import bpy  # pylint: disable=import-error

import celestine
from celestine import load
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
    F,
    N,
    S,
    T,
)
from celestine.window.element import Abstract as Abstract_
from celestine.window.element import Button as Button_
from celestine.window.element import Image as Image_
from celestine.window.element import Label as Label_
from celestine.window.window import Window as Window_

COLLECTION = _collection


INTERFACE = "interface"
BLENDER = "blender"
PACKAGE = "package"
PREFERENCES = "preferences"


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
        Image.start()
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
        Image.finish()
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

    def center_float(self) -> T[F, F]:
        """"""
        x_dot = (self.x_min + self.x_max) / 2
        y_dot = (self.y_min + self.y_max) / 2
        return (x_dot, y_dot)

    def render(self) -> N:
        """"""
        (x_dot, y_dot) = self.center_float()
        # child sets mesh and then calls this
        self.item.location = (x_dot, y_dot, 0)
        self.item.rotation = (180, 0, 0)


class Mouse(Abstract):
    """"""

    def __init__(self, mesh) -> N:
        self.mesh = mesh.soul
        self.text = "mouse"
        super().__init__("mouse")
        self.item = mesh

    def draw(self, view: COLLECTION) -> N:
        """"""

        diamond = Diamond()
        diamond.make(self.mesh)

        self.render()


class Button(Abstract, Button_):
    """"""

    def draw(self, view: COLLECTION, *, make: B, **star) -> N:
        """"""
        if not make:
            return

        width = len(self.data) / 4
        height = 1 / 20

        plane = quadrilateral.plane(view, self.data)
        plane.scale = (width, height, 1)

        text = basic.text(view, self.data, self.data)
        text.scale = (1 / width, 1 / height, 1)
        text.location = (-width / 4, -height, 0.1)

        text.parent = plane

        self.item = plane
        self.render()


class Image(Abstract, Image_):
    """"""

    default: data.image

    @classmethod
    def start(cls):
        """"""
        name = "null.png"
        path = load.pathway.asset(name)
        cls.default = data.image.load(path)

    @classmethod
    def finish(cls):
        """"""
        item = cls.default
        data.image.remove(item)
        cls.default = None

    def draw(self, view: COLLECTION, *, make: B, **star) -> N:
        """"""
        if not make:
            return

        path = self.image or load.pathway.asset("null.png")
        image = data.image.load(path)
        material = UV.image(self.tag, image)
        plane = basic.image(view, self.tag, image.size)

        plane.body.data.materials.append(material)
        self.item = plane
        self.render()

    def update(self, *, image: S, **star) -> B:
        """"""
        if not super().update(image=image, **star):
            return False

        material = bpy.data.materials[self.tag]
        node = material.node_tree.nodes["Image Texture"]
        node.image = data.image.load(image)

        return True


class Label(Abstract, Label_):
    """"""

    def draw(self, view: COLLECTION, *, make: B, **star) -> N:
        """"""
        if not make:
            return

        self.item = basic.text(view, self.data, self.data)
        self.render()


class Window(Window_):
    """"""

    def data(self, container):
        """"""
        collection = data.collection.make(container.tag)
        collection.hide()
        container.data = collection

    def poke(self, **star):
        """"""
        page = bpy.context.scene.celestine.page
        item = self._view.get(page)
        item.poke(**star)

    def page(self, name, document):
        """"""
        page = self.container.drop(name)
        document(page)
        page.spot(0, 0, self.width, self.height)

        self.item_set(name, page)

        self.frame = name

    def item_find(self, page):
        """"""
        for name, item in bpy.data.collections.items():
            if page == name:
                return item

    def turn(self, page, **star):
        """"""
        name = bpy.context.scene.celestine.page
        item = self.item_find(name)
        item.hide_render = True
        item.hide_viewport = True

        item = self.item_find(page)
        item.hide_render = False
        item.hide_viewport = False
        bpy.context.scene.celestine.page = page

    def view(self, name, function):
        """"""
        super().view(name, function)
        self.page = self._view.get(name)
        self.draw(make=True)

    def __enter__(self):
        if self.call:
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

        self.mouse = Mouse(mesh)
        self.mouse.draw(collection)

        @classmethod
        def bind(cls, collection, name, soul):
            """Give an existing soul a body."""
            body = bpy.data.objects.new(name, soul)
            collection.objects.link(body)
            return cls(body, soul)

        override = context()
        bpy.ops.view3d.toggle_shading(override, type="RENDERED")
        bpy.ops.view3d.view_camera(override)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.call:
            call = getattr(self, self.call)
            call(**self.star)
            return False

        # yes super must go after
        super().__exit__(exc_type, exc_value, traceback)
        return False

    def __init__(self, session, element, size, *, call=None, **star):
        super().__init__(session, element, size, **star)
        self.frame = None
        self.mouse = None

        self.call = call
        self.star = star


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
    element = {
        "button": Button,
        "image": Image,
        "label": Label,
    }
    size = (20, 20)
    return Window(session, element, size, **star)
