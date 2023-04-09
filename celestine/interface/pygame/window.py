""""""

from celestine import load
from celestine.window.container import Container
from celestine.window.window import Window as window

from . import package
from .element import (
    Button,
    Image,
    Label,
)


class Window(window):
    """"""

    def data(self, container):
        """"""
        container.data = self.book

    def draw(self, **star):
        """"""
        self.book.fill((0, 0, 0))

        super().draw(font=self.font, **star)

        package.display.flip()

    def __enter__(self):
        super().__enter__()
        package.init()
        self.book = package.display.set_mode(
            (self.width, self.height), 8, 0
        )
        path = load.pathway("asset", "CascadiaCode.ttf")
        self.font = package.font.Font(path, 40)

        self.container = Container(
            self.session,
            "window",
            self,
            Button,
            Image,
            Label,
            x_min=0,
            y_min=0,
            x_max=self.width,
            y_max=self.height,
            offset_x=0,
            offset_y=0,
        )

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        while True:
            event = package.event.wait()
            match event.type:
                case package.QUIT:
                    break
                case package.MOUSEBUTTONDOWN:
                    (x_dot, y_dot) = package.mouse.get_pos()
                    self.page.poke(x_dot, y_dot)
        return False

    def __init__(self, session, **star):
        super().__init__(session, **star)
        self.book = None
        self.container = None
        self.font = None
        self.width = 1280
        self.height = 960
