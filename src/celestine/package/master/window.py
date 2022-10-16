from .collection import Collection


class Window(Collection):
    def page(self, document):
        pass

    def turn(self, page):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.turn(0)
        return False

    def __init__(self, session):
        super().__init__()
        self.session = session
