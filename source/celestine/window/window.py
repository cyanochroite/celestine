from .collection import Collection


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
            self.turn(0)
        except AttributeError as error:
            message = "Application has no functions whatsoever."
            raise RuntimeError(message) from error
        except KeyError as error:
            message = "No main function (return value of 0) found."
            raise RuntimeError(message) from error
        return False

    def __init__(self, session, **kwargs):
        super().__init__(**kwargs)
        self.session = session

