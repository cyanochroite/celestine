""""""

from celestine.typed import (
    L,
    S,
)

from .collection import Collection2
from .container import Container


class Window:
    """"""

    def data(self, container):
        """"""

    def draw(self, **star):
        """"""
        star.update(ring=self.ring)
        self.page.draw(self.page.data, **star)

    def code(self, name, function):
        """"""
        self.task.set(name, function)

    def view(self, name, function):
        """"""
        container = self.container.drop(name)
        self.data(container)
        function(self.ring, container)
        container.spot(0, 0, self.width, self.height)
        self._view.set(name, container)

    def extension(self) -> L[S]:
        """"""
        return [
            ".bmp",
            ".sgi",
            ".rgb",
            ".bw",
            ".png",
            ".jpg",
            ".jpeg",
            ".jp2",
            ".j2c",
            ".tga",
            ".cin",
            ".dpx",
            ".exr",
            ".hdr",
            ".tif",
            ".tiff",
            ".webp",
            ".pbm",
            ".pgm",
            ".ppm",
            ".pnm",
            ".gif",
            ".png",
        ]

    def turn(self, page, **star):
        """"""
        self.page = self._view.get(page)
        self.turn_page = page
        self.draw(make=True)

    def work(self, task, **star):
        """"""
        star.update(ring=self.ring)
        caller = self.task.get(task)
        caller(**star)
        self.draw(make=False)

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

    def __init__(self, ring, element, size, **star):
        self.ring = ring
        self.turn_page = ring.main
        self.page = None
        self.task = Collection2()
        self._view = Collection2()

        (self.width, self.height) = size

        self.container = Container(
            self.ring,
            "window",
            self,
            element,
            x_min=0,
            y_min=0,
            x_max=self.width,
            y_max=self.height,
            offset_x=0,
            offset_y=0,
        )
