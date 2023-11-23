""""""

from celestine.typed import (
    LS,
    A,
    D,
    H,
    K,
    N,
    R,
    S,
)
from celestine.window.container import View


class Window(View):
    """"""

    hold: H
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

    def hide(self):
        pass

    def show(self):
        self.page.show()

    def turn(self, page: S) -> N:
        """"""
        self.page.hide()
        self.page = self.view[page]
        self.page.show()
        self.draw()

    def work(self, code, **star: R):
        """"""
        caller = self.code.get(code)
        caller(self.hold, **star)
        self.draw(**star)

    def __enter__(self) -> K:
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.spot(self.area)
        self.make()
        self.draw()
        if exc_type:
            raise exc_type
        if exc_value:
            raise exc_value
        if traceback:
            raise traceback
        return False

    def __init__(self, hold: H, canvas, element, **star: R) -> N:
        self.hold = hold
        self.page = self
        self.code = {}
        self.view = {}

        super().__init__(
            self.hold,
            canvas,
            "window",
            self,
            element,
        )
