from .package.data import mesh as make_mesh
from .package import mesh as _mesh

from .element import Element


class Button(Element):
    def __init__(self, text, action, **kwargs):
        self.text = text
        super().__init__(**kwargs)
        self.action = action

    def draw(self, collection):
        width = len(self.text) / 4
        height = 1 / 20

        plane = _mesh.plane(self.text)
        mesh = make_mesh.bind(collection, self.text, plane)
        mesh.scale = (width, height, 1)

        word = _mesh.text(collection, self.text, self.text)
        word.scale = (1 / width, 1 / height, 1)
        word.location = (- width / 4, - height, 0.1)

        word.parent = mesh

        self.mesh = mesh
        super().draw(collection)

    def poke(self, x_dot, y_dot):
        """"""
        if super().poke(x_dot, y_dot):
            self.action()
