""""""

from celestine import load
from celestine.window.window import Window as window

from . import package


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
        def set_caption():
            caption = self.session.language.APPLICATION_TITLE
            package.display.set_caption(caption)

        def set_font():
            package.font.init()
            file_path = load.asset("CascadiaCode.ttf")
            size = 40
            self.font = package.font.Font(file_path, size)

        def set_icon():
            path = "icon.png"
            asset = load.asset(path)
            image = package.image.load(asset)
            icon = image.convert_alpha()
            package.display.set_icon(icon)

        def set_mode():
            size = (self.width, self.height)
            self.book = package.display.set_mode(size)

        super().__enter__()
        set_mode()
        set_icon()
        set_caption()
        set_font()
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

        package.quit()
        return False

    def __init__(self, session, element, size, **star):
        super().__init__(session, element, size, **star)
        self.book = None
        self.font = None
