""""""

from .collection import Collection2


class Window():
    """"""

    def data(self, container):
        """"""

    def draw(self, **star):
        """"""
        self.page.draw(self.page.data, **star)

    def view(self, name, document):
        """"""
        container = self.container.drop(name)
        self.data(container)
        document(container)
        container.spot(0, 0, self.width, self.height)
        self._view.set(name, container)

    def turn(self, page, **star):
        """"""
        self.page = self._view.get(page)
        self.turn_page = page
        self.draw()

    def work(self, task, **star):
        """"""
        call = self.task.get(task)
        call(**star)
        self.draw()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            raise exc_type
        try:
            self.turn(self.turn_page)
        except AttributeError as error:
            message = "Application has no functions whatsoever."
            raise RuntimeError(message) from error
        except KeyError as error:
            page = self.turn_page
            message = f"Missing function called {page}."
            raise RuntimeError(message) from error
        return False

    def __init__(self, session, **star):
        self.session = session
        self.turn_page = session.main
        self.page = None
        self.task = Collection2()
        self._view = Collection2()
        self.container = None
        self.width = 1920
        self.height = 1080
        super().__init__(**star)
