""""""

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
        container.data = package.Frame(
            self.root,
            padx=5,
            pady=5,
            bg="skyblue",
            width=1920,
            height=1080,
        )
        container.data.place(x=0, y=0)

    def turn(self, page, **star):
        super().turn(page, **star)
        self.page.data.tkraise()

    def __enter__(self):
        super().__enter__()
        self.root.title(self.session.language.APPLICATION_TITLE)
        self.root.geometry("1920x1080")
        self.root.minsize(640, 480)
        self.root.maxsize(3840, 2160)
        self.root.config(bg="blue")

        self.container = Container(
            self.session,
            "window",
            self,
            Button,
            Image,
            Label,
            x_min=0,
            y_min=0,
            x_max=640,
            y_max=2160,
            offset_x=0,
            offset_y=0,
        )

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        self.root.mainloop()
        return False

    def __init__(self, session, **star):
        super().__init__(session, **star)
        self.root = package.Tk()
        self.width = 1920
        self.height = 1080
