from .collection import Rectangle


class Page(Rectangle):
    def line(self, tag):
        pass

    def __init__(self, session, **kwargs):
        super().__init__(**kwargs)
        self.session = session
