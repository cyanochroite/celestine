""""""

from .container import Drop

from celestine.window.window import Window as master

from celestine.window.collection import Rectangle

from celestine import load

from .page import Page

from . import package


class Window(master):
    def page(self, name, document):
        self.item_set(name, document)

        page = Drop(
            self.session,
            name,
            self.turn,
            self.font,
            x_min=0,
            y_min=0,
            x_max=1280,
            y_max=960,
            offset_x=0,
            offset_y=0,
        )

        self.frame = page

    def turn(self, page):
        page2 = Drop(
            self.session,
            page,
            self.turn,
            self.font,
            x_min=0,
            y_min=0,
            x_max=1280,
            y_max=960,
            offset_x=0,
            offset_y=0,
        )
        self.book.fill((0, 0, 0))

        self.frame = page2
        self.item_get(page)(page2)

        page2.draw(self.book)

        package.display.flip()

    def __enter__(self):
        super().__enter__()
        package.init()
        self.book = package.display.set_mode((self.width, self.height), 8, 0)
        path = load.pathway("asset", "CascadiaCode.ttf")
        self.font = package.font.Font(path, 40)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        while True:
            match package.event.wait().type:
                case package.QUIT:
                    break
                case package.MOUSEBUTTONDOWN:
                    self.frame.select(*package.mouse.get_pos())
        return False

    def __init__(self, session, **kwargs):
        super().__init__(session, **kwargs)
        self.book = None
        self.frame = None
        self.width = 1280
        self.height = 960
