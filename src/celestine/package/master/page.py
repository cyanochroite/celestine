from .collection import Rectangle


class Page(Rectangle):
    def line(self, tag):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
