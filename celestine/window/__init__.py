""""""

from celestine.typed import (
    LS,
    A,
    D,
    N,
    R,
    S,
)

from .container import (
    View,
    Zone,
)


class Window(View):
    """"""

    ring: R
    page: View
    code: D[S, A]  # function
    view: D[S, View]

    def setup(self, name: S) -> A:
        """"""
        return self.canvas

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

    def turn(self, page: S, **star) -> N:
        """"""
        self.page.hidden = True
        self.page = self.view.get(page)
        self.page.hidden = False
        self.draw(**star)

    def work(self, code, **star):
        """"""
        caller = self.code.get(code)
        caller(ring=self.ring, **star)
        self.draw(**star)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.spot(self.area)
        self.make()
        if exc_type:
            raise exc_type
        try:
            turn_page = self.ring.main
            self.page = self.view.get(turn_page)
            self.turn(turn_page)
        except AttributeError as error:
            message = "Application has no functions whatsoever."
            raise RuntimeError(message) from error
        except KeyError as error:
            message = "Missing 'main' function."
            raise RuntimeError(message) from error
        return False

    def __getitem__(self, key: S):
        return self.view[key]

    def __init__(self, ring, canvas, element, area, **star):
        self.ring = ring
        self.page = None
        self.code = {}
        self.view = {}

        super().__init__(
            self.ring,
            canvas,
            "window",
            self,
            element,
            area,
        )

    def __setitem__(self, key: S, value: A):
        container = self.zone(key, mode=Zone.DROP)
        container.canvas = self.setup(key)
        container.hidden = True
        value(container)
        self.view[key] = container
