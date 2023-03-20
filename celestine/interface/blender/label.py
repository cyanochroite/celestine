""""""

from celestine.window.label import Label as label

from .element import Element
from .package import mesh as _mesh


class Label(label, Element):
    """"""

    def draw(self, collection):
        self.item = _mesh.text(collection, self.text, self.text)
        super().draw(collection)
