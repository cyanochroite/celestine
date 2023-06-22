""""""

from celestine.typed import (
    L,
    S,
)

from .collection import Collection2
from .container import (
    View,
    Zone,
)


class Window(View):
    """"""

    def setup(self, container):
        """"""
        container.canvas = self.canvas

    def draw(self, **star):
        """"""
        self.page.draw(self.ring, self.page.canvas, **star)

    def code(self, name, function):
        """"""
        self.task.set(name, function)

    def view(self, name, function):
        """"""
        container = self.zone(name, mode=Zone.DROP)
        self.setup(container)
        function(self.ring, container)
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
        self.spot(self.area)
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

    def __init__(self, ring, element, area, **star):
        self.ring = ring
        self.turn_page = ring.main
        self.page = None
        self.task = Collection2()
        self._view = Collection2()

        super().__init__(
            self.ring,
            "window",
            self,
            element,
            area,
            offset_x=0,
            offset_y=0,
        )
