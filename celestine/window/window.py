""""""

from .collection import Collection
from .collection import Collection2


class Window(Collection):
    """"""

    def page(self, name, document):
        """"""

    def turn(self, page):
        """"""

    def work(self, task):
        """"""
        call = self.task.get(task)
        call()

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
        self.task = Collection2()
        super().__init__(**star)
