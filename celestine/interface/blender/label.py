from .package.data import mesh as make_mesh
from .package import mesh as _mesh

from .element import Element


class Label(Element):
    def __init__(self, text, **kwargs):
        self.text = text
        super().__init__(**kwargs)

    def draw(self, collection):
        self.mesh = _mesh.text(collection, self.text, self.text)
        super().draw(collection)
