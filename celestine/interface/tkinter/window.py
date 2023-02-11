from celestine.window.window import Window as master

from . import package
from . import package
from .page import Page

from .container import Drop


class Window(master):
    def page(self, name, document):
        page = Drop(
            self.session,
            name,
            self.turn,
            x_min=0,
            y_min=0,
            x_max=20,
            y_max=20,
            offset_x=0,
            offset_y=2.5,
        )
        document(page)

        frame = package.Frame(
            self.root,
            padx=5,
            pady=5,
            bg="skyblue",
        )
        frame.grid(row=0, column=0, sticky="nsew")
        page.draw(frame)
        self.item_set(name, frame)

    def turn(self, page):
        frame = self.item_get(page)
        frame.tkraise()

    def __enter__(self):
        super().__enter__()
        self.root.title(self.session.language.APPLICATION_TITLE)
        self.root.geometry("1920x1080")
        self.root.minsize(640, 480)
        self.root.maxsize(3840, 2160)
        self.root.config(bg="blue")
        return self

    def collection(self, name):
        """"""
        frame = package.Frame(
            self.root,
            padx=5,
            pady=5,
            bg="skyblue",
        )
        frame.grid(row=0, column=0, sticky="nsew")
        self.item_set(name, frame)
        return frame

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        self.root.mainloop()
        return False

    def __init__(self, session, **kwargs):
        super().__init__(session, **kwargs)
        self.root = package.Tk()
