# <pep8-80 compliant>
"""Package celestine."""
import bpy  # pylint: disable=import-error
import bmesh  # pylint: disable=import-error

from celestine.package.blender.package import data
from celestine.package.blender.package import preferences
from celestine.package.blender.package import UV


from celestine.package.master import Window as Window_


def new_image(image):
    mesh = bmesh.new(use_operators=False)

    mesh.verts.new((+1, +1, +0))
    mesh.verts.new((-1, +1, +0))
    mesh.verts.new((-1, -1, +0))
    mesh.verts.new((+1, -1, +0))
    mesh.verts.ensure_lookup_table()

    mesh.edges.new((mesh.verts[0], mesh.verts[1]))
    mesh.edges.new((mesh.verts[1], mesh.verts[2]))
    mesh.edges.new((mesh.verts[2], mesh.verts[3]))
    mesh.edges.new((mesh.verts[3], mesh.verts[0]))
    mesh.edges.ensure_lookup_table()

    mesh.faces.new((
        mesh.verts[0],
        mesh.verts[1],
        mesh.verts[2],
        mesh.verts[3],
    ))
    mesh.faces.ensure_lookup_table()

    uv = mesh.loops.layers.uv.verify()  # ANOCE
    (x, y) = image.size
    (x, y) = ((max(y / x, 1) - 1) / 2, (max(x / y, 1) - 1) / 2)
    mesh.faces[0].loops[0][uv].uv = (1 + x, 1 + y)
    mesh.faces[0].loops[1][uv].uv = (0 - x, 1 + y)
    mesh.faces[0].loops[2][uv].uv = (0 - x, 0 - y)
    mesh.faces[0].loops[3][uv].uv = (1 + x, 0 - y)

    meshit = bpy.data.meshes.new("name")
    mesh.to_mesh(meshit)
    mesh.free()
    return meshit


class Image():
    """Holds an image."""

    def __init__(self, file):
        _image = data.image.load(file)
        self.height = _image.size[1]
        self.image = _image
        self.width = _image.size[0]
        self.name = file


spot = 0


def __new_object(image):
    global spot
    mush = new_image(image)
    box = data.mesh.make("image", mush)
    box.location = (spot, 0, 0)
    spot += 2.5
    return box


def __image(tag, _image):
    """pass"""
    image = _image.image
    material = UV.material("pretty", image)
    object = _new_object(image)
    object.data.materials.append(material)


def image_load(file):
    """pass"""
    print("convert " + file)
    return Image(file)


class Widget():
    def __init__(self, name, mesh, location):
        self.item = data.mesh.make(name, mesh)
        self.item.location = location


class Button(Widget):
    def __init__(self, frame, text, command):
        super().__init__(
            tkinter.Button(
                frame,
                text=text,
                command=command,
            )
        )


class Image(Widget):
    def __init__(self, frame, file):
        image = tkinter.PhotoImage(file=file)
        self.height = image.height()
        self.image = image
        self.width = image.width()
        self.name = file
        super().__init__(
            tkinter.Label(
                frame,
                image=image,
            )
        )


class Label(Widget):
    def __init__(self, name, text, location):
        mesh = bmesh.new(use_operators=False)

        mesh.verts.new((+1, +1, +0))
        mesh.verts.new((-1, +1, +0))
        mesh.verts.new((-1, -1, +0))
        mesh.verts.new((+1, -1, +0))
        mesh.verts.ensure_lookup_table()

        mesh.edges.new((mesh.verts[0], mesh.verts[1]))
        mesh.edges.new((mesh.verts[1], mesh.verts[2]))
        mesh.edges.new((mesh.verts[2], mesh.verts[3]))
        mesh.edges.new((mesh.verts[3], mesh.verts[0]))
        mesh.edges.ensure_lookup_table()

        mesh.faces.new((
            mesh.verts[0],
            mesh.verts[1],
            mesh.verts[2],
            mesh.verts[3],
        ))
        mesh.faces.ensure_lookup_table()

        uv = mesh.loops.layers.uv.verify()

        mesh.faces[0].loops[0][uv].uv = (1, 1)
        mesh.faces[0].loops[1][uv].uv = (0, 1)
        mesh.faces[0].loops[2][uv].uv = (0, 0)
        mesh.faces[0].loops[3][uv].uv = (1, 0)

        meshit = bpy.data.meshes.new(name)
        mesh.to_mesh(meshit)
        mesh.free()

        super().__init__(name, meshit, location)


class Button(Widget):
    def __init__(self, name, text, location):
        mesh = bmesh.new(use_operators=False)

        mesh.verts.new((+1, +1, +0))
        mesh.verts.new((-1, +1, +0))
        mesh.verts.new((-1, -1, +0))
        mesh.verts.new((+1, -1, +0))
        mesh.verts.ensure_lookup_table()

        mesh.edges.new((mesh.verts[0], mesh.verts[1]))
        mesh.edges.new((mesh.verts[1], mesh.verts[2]))
        mesh.edges.new((mesh.verts[2], mesh.verts[3]))
        mesh.edges.new((mesh.verts[3], mesh.verts[0]))
        mesh.edges.ensure_lookup_table()

        mesh.faces.new((
            mesh.verts[0],
            mesh.verts[1],
            mesh.verts[2],
            mesh.verts[3],
        ))
        mesh.faces.ensure_lookup_table()

        uv = mesh.loops.layers.uv.verify()

        mesh.faces[0].loops[0][uv].uv = (1, 1)
        mesh.faces[0].loops[1][uv].uv = (0, 1)
        mesh.faces[0].loops[2][uv].uv = (0, 0)
        mesh.faces[0].loops[3][uv].uv = (1, 0)

        meshit = bpy.data.meshes.new(name)
        mesh.to_mesh(meshit)
        mesh.free()

        super().__init__(name, meshit, location)


class Frame():
    def item_get(self, tag):
        return self.item[tag]

    def item_set(self, tag, value):
        self.item[tag] = value
        return value

    def __init__(self, window):
        self.window = window
        self.item = {}
        self.frame = 0

    def __enter__(self):
        # clear
        for material in bpy.data.materials:
            data.material.remove(material)
        for mesh in bpy.data.meshes:
            data.mesh.remove(mesh)
        for image in bpy.data.images:
            data.image.remove(image)
        for texture in bpy.data.textures:
            data.texture.remove(texture)
        return self

    def __exit__(self, *_):
        return False

    def row(self, tag):
        item = Row(self, tag, self.frame)
        self.frame -= 2.5
        return self.item_set(tag, item)


class Row():
    def __init__(self, frame, tag, offset_y):
        self.frame = frame
        self.tag = tag
        self.cord_x = 0
        self.cord_y = offset_y

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def draw(self):
        location = (self.cord_x, self.cord_y, 0)
        self.cord_x += 2.5
        return location

    def button(self, tag, label, action):
        return self.frame.item_set(
            tag,
            Button(
                label,
                lambda: self.frame.window.show_frame(action),
                self.draw(),
            ),
        )

    def image(self, tag, file):
        return self.frame.item_set(
            tag,
            Image(
                self.row,
                tag,
                file,
            ),
        )

    def label(self, tag, text):
        return self.frame.item_set(
            tag,
            Label(
                tag,
                text,
                self.draw(),
            ),
        )


class Window(Window_):

    def __init__(self, session):
        super().__init__(session)
        self.window = 0

    def show_frame(self, index):
        self.window = index

    def frame(self):
        return Frame(self)

    def __enter__(self):
        try:
            data.register()
            preferences.register()
        except ValueError:
            # register_class(...): already registered as a subclass
            pass

        for camera in bpy.data.cameras:
            data.camera.remove(camera)
        for light in bpy.data.lights:
            data.light.remove(light)
        for material in bpy.data.materials:
            data.material.remove(material)
        for mesh in bpy.data.meshes:
            data.mesh.remove(mesh)
        for image in bpy.data.images:
            data.image.remove(image)
        for texture in bpy.data.textures:
            data.texture.remove(texture)

        light = data.light.sun.make("light")
        light.location = (0, 0, 1)

        camera = data.camera.make("camera")
        camera.location = (+20, -10, +60)
        return self

    def __exit__(self, *_):
        return False

