""""""

from celestine import load
from celestine.window.window import Window as master

from . import package
from .button import Button
from .container import (
    Container,
    Drop,
    Grid,
    Span,
)
from .image import Image
from .label import Label


class Window(master):
    """"""

    def page(self, name, document):
        self.item_set(name, document)

    def turn(self, page, **star):
        self.frame = self.container.drop(page)
        self.item_get(page)(self.frame)
        self.frame.spot(0, 0, self.width, self.height)
        self.book.fill((0, 0, 0))
        self.frame.draw(self.book)
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
            self.font,
            Button,
            Image,
            Label,
            Drop,
            Grid,
            Span,
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
                    self.frame.poke(x_dot, y_dot)
        return False

    def __init__(self, session, **star):
        super().__init__(session, **star)
        self.book = None
        self.container = None
        self.font = None
        self.frame = None
        self.width = 1280
        self.height = 960
