from celestine.window.window import Window as master

from . import package
from .page import Page


class Window(master):
    def page(self, document):
        page = Page(self)
        page.frame.grid(row=0, column=0, sticky="nsew")
        index = len(self.item)
        self.item_set(index, page)
        document(page)
        return page

    def turn(self, page):
        frame = self.item_get(page)
        frame.frame.tkraise()

    def __enter__(self):
        super().__enter__()
        self.root = package.Tk()
        self.root.title(self.session.language.APPLICATION_TITLE)
        self.root.geometry("1920x1080")
        self.root.minsize(640, 480)
        self.root.maxsize(3840, 2160)
        self.root.config(bg="blue")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        self.root.mainloop()
        return False

    def __init__(self, session, **kwargs):
        super().__init__(session, **kwargs)
        self.root = None
