""""""

from celestine.window.label import Label as label

from .element import Element


from .package import mesh as _mesh


class Label(Element, label):


class Label(Element):
    """"""

    def draw(self, collection):
        self.mesh = _mesh.text(collection, self.text, self.text)
        super().draw(collection)

    def __init__(self, text, **kwargs):
        self.text = text
        super().__init__(**kwargs)
