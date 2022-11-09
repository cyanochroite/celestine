from celestine.window.window import Window as master

from celestine.window.collection import Rectangle
from celestine.package.blender.package import data

import bpy

from . import package
from .page import Page
from .mouse import Mouse


def context():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            override = bpy.context.copy()
            override['area'] = area
            return override
    return None


class Window(master):
    def page(self, document):
        index = len(self.item)
        self.item_set(index, document)
        rectangle = Rectangle(0, 0, 20, 10, 0, 0)
        page = Page(self, rectangle)
        self.frame = page
        return page

    def turn(self, page):
        rectangle = Rectangle(0, 0, 20, 10, 0, 0)
        page2 = Page(self, rectangle)
        self.frame = page2
        self.item_get(page)(page2)

    def __enter__(self):
        super().__enter__()
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

        camera = data.camera.make("camera")
        camera.location = (+16.0, -08.5, +60.0)
        camera.ortho_scale = +35.0
        camera.type = 'ORTHO'

        light = data.light.sun.make("light")
        light.location = (0, 0, 1)

        self.mouse = Mouse(Rectangle())

        override = context()
        bpy.ops.view3d.toggle_shading(override, type='RENDERED')
        bpy.ops.view3d.view_camera(override)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        return False

    def __init__(self, session, **kwargs):
        super().__init__(session, **kwargs)
        self.frame = None
        self.width = 20
        self.height = 10
        self.mouse = None
