""""""

from celestine.window.window import Window as master

from celestine import load

from . import package

from .container import Container


class Window(master):
    """"""

    def page(self, name, document):
        self.item_set(name, document)

    def turn(self, page):
        self.frame = self.container.drop(page)
        self.book.fill((0, 0, 0))
        self.item_get(page)(self.frame)
        self.frame.draw(self.book)
        package.display.flip()

    def __enter__(self):
        super().__enter__()
        package.init()
        self.book = package.display.set_mode((self.width, self.height), 8, 0)
        path = load.pathway("asset", "CascadiaCode.ttf")
        self.font = package.font.Font(path, 40)

        self.container = Container(
            self.session,
            "window",
            self.turn,
            self.font,
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
            match package.event.wait().type:
                case package.QUIT:
                    break
                case package.MOUSEBUTTONDOWN:
                    self.frame.select(*package.mouse.get_pos())
        return False

    def __init__(self, session, **kwargs):
        super().__init__(session, **kwargs)
        self.book = None
        self.container = None
        self.font = None
        self.frame = None
        self.width = 1280
        self.height = 960
