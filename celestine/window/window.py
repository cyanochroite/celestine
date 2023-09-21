""""""

from abc import (
    ABC,
    abstractmethod,
)

from celestine.typed import (
    LS,
    A,
    S,
)

from .collection import Collection2
from .container import (
    View,
    Zone,
)


class Window(ABC, View):
    """"""

    @abstractmethod
    def setup(self, name: S) -> A:
        ...

    def code(self, name, function):
        """"""
        self.task.set(name, function)

    def view(self, name, function):
        """"""
        container = self.zone(name, mode=Zone.DROP)
        container.canvas = self.setup(name)
        container.hidden = True
        function(self.ring, container)
        self._view.set(name, container)

    def extension(self) -> LS:
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
        self.page.hidden = True
        self.page = self._view.get(page)
        self.page.hidden = False

        self.turn_page = page
        self.draw(self.ring, **star)

    def work(self, task, **star):
        """"""
        caller = self.task.get(task)
        caller(ring=self.ring, **star)
        self.draw(self.ring, **star)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.spot(self.area)
        self.make(self.ring)
        if exc_type:
            raise exc_type
        try:
            self.page = self._view.get(self.turn_page)
            self.turn(self.turn_page)
        except AttributeError as error:
            message = "Application has no functions whatsoever."
            raise RuntimeError(message) from error
        except KeyError as error:
            page = self.turn_page
            message = f"Missing function called {page}."
            raise RuntimeError(message) from error
        return False

    def __init__(self, ring, canvas, element, area, **star):
        self.ring = ring
        self.turn_page = ring.main
        self.page = None
        self.task = Collection2()
        self._view = Collection2()

        super().__init__(
            self.ring,
            canvas,
            "window",
            self,
            element,
            area,
            offset_x=0,
            offset_y=0,
        )
