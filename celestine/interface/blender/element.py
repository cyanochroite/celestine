""""""

from celestine import load
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

from .package import (
    UV,
    data,
)
from .package import mesh as _mesh
from .package.data import mesh as make_mesh
from .package.data.collection import _collection

COLLECTION = _collection


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


class Button(Abstract, Button_):
    """"""

    def draw(self, view: COLLECTION, *, make: B, **star) -> N:
        """"""
        if not make:
            return

        width = len(self.data) / 4
        height = 1 / 20

        plane = _mesh.quadrilateral.plane(view, self.data)
        plane.scale = (width, height, 1)

        text = _mesh.text(view, self.data, self.data)
        text.scale = (1 / width, 1 / height, 1)
        text.location = (-width / 4, -height, 0.1)

        text.parent = plane

        self.item = plane
        self.render()


class Image(Abstract, Image_):
    """"""

    def draw(self, view: COLLECTION, *, make: B, **star) -> N:
        """"""
        if not make:
            return

        path = self.image or load.asset("null.png")
        _image = data.image.load(path)
        material = UV.material("pretty", _image)
        plane = _mesh.image(_image)
        mesh = make_mesh.bind(view, path, plane)
        mesh.body.data.materials.append(material)
        self.item = mesh
        self.render()

    def update(self, *, image: S, **star) -> B:
        """"""
        if not super().update(image=image, **star):
            return False

        _image = data.image.load(self.image)
        material = UV.material("pretty", _image)
        self.item.body.data.materials.clear()
        self.item.body.data.materials.append(material)
        return True


class Label(Abstract, Label_):
    """"""

    def draw(self, view: COLLECTION, *, make: B, **star) -> N:
        """"""
        if not make:
            return

        self.item = _mesh.text(view, self.data, self.data)
        self.render()
