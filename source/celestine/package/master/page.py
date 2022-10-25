from .collection import Rectangle


class Page(Rectangle):
    def line(self, tag):
        pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
