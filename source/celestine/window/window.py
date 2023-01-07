from .collection import Collection
from celestine import load

from celestine.window.page import Page


class Window(Collection):
    def page(self, document):
        pass

    def turn(self, page):
        pass

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
            message = F"Missing function called {page}."
            raise RuntimeError(message) from error
        return False

    def __init__(self, session, **kwargs):
        super().__init__(**kwargs)
        self.session = session
        self.turn_page = session.main
