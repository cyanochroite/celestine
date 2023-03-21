""""""

from celestine.window.element import Abstract as abstract
from celestine.window.element import Button as button
from celestine.window.element import Image as image
from celestine.window.element import Label as label

from .package import (
    UV,
    data,
)
from .package import mesh as _mesh
from .package.data import mesh as make_mesh

# TODO: finish this


class Abstract(abstract):
    """"""

    def center_float(self):
        """"""
        x_dot = (self.x_min + self.x_max) / 2
        y_dot = (self.y_min + self.y_max) / 2
        return (x_dot, y_dot)

    def draw(self, collection):
        """"""
        (x_dot, y_dot) = self.center_float()
        # child sets mesh and then calls this
        self.item.location = (x_dot, y_dot, 0)
        self.item.rotation = (180, 0, 0)


class Button(Abstract, button):
    """"""

    def draw(self, collection):
        width = len(self.text) / 4
        height = 1 / 20

        plane = _mesh.plane(self.text)
        mesh = make_mesh.bind(collection, self.text, plane)
        mesh.scale = (width, height, 1)

        word = _mesh.text(collection, self.text, self.text)
        word.scale = (1 / width, 1 / height, 1)
        word.location = (-width / 4, -height, 0.1)

        word.parent = mesh

        self.item = mesh
        super().draw(collection)


class Image(Abstract, image):
    """"""

    def draw(self, collection):
        _image = data.image.load(self.image)
        material = UV.material("pretty", _image)
        plane = _mesh.image(_image)
        mesh = make_mesh.bind(collection, self.image, plane)
        mesh.body.data.materials.append(material)
        self.item = mesh
        super().draw(collection)


class Label(Abstract, label):
    """"""

    def draw(self, collection):
        self.item = _mesh.text(collection, self.text, self.text)
        super().draw(collection)
