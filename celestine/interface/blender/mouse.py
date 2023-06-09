""""""

from celestine.package.blender.data.collection import _collection
from celestine.typed import N

from .element import Abstract

COLLECTION = _collection

from celestine.package.blender.mesh.quadrilateral import Diamond


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

        # self.item = make_mesh.bind(view, self.text, self.mesh)

        self.render()
