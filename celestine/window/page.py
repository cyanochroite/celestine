""""""

from .collection import Rectangle
from .line import Line


class Page(Rectangle):
    """"""

    def line(
        self,
        tag: str
    ) -> Line:
        """"""

        return self.item_set(tag, Line(self, tag))

    def __init__(self, session, frame=None, **kwargs):
        self.session = session
        self.frame = frame
        super().__init__(**kwargs)
