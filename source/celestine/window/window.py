from .collection import Collection
from celestine.session import load

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
            message = F"Missing function with return value of {page}."
            raise RuntimeError(message) from error
        return False

    def _turn_page(self, session):
        dictionary_int = {}
        dictionary_str = {}
        function = load.function(session.application)
        for (key, value) in function.items():
            index = value(Page(self.session, None))
            dictionary_int[index] = key
            dictionary_str[key] = index
        value_int = dictionary_int.get(session.main, None)
        value_str = dictionary_str.get(session.main, None)
        return value_int or value_str

    def __init__(self, session, **kwargs):
        super().__init__(**kwargs)
        self.session = session
        self.turn_page = self._turn_page(session)
