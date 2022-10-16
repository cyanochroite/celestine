from celestine.package.master.window import Window as master

from . import package
from .page import Page


class Window(master):
    def page(self, document):
        page = Page(self)
        index = len(self.item)
        self.item_set(index, page)
        return page

    def turn(self, page):
        frame = self.item_get(page)
        frame.frame.tkraise()

    def __enter__(self):
        self.root = package.Tk()
        self.root.title(self.session.language.APPLICATION_TITLE)
        self.root.geometry("1920x1080")
        self.root.minsize(640, 480)
        self.root.maxsize(3840, 2160)
        self.root.config(bg="blue")
        return super().__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        self.root.mainloop()
        return super().__exit__(exc_type, exc_value, traceback)

    def __init__(self, session):
        super().__init__(session)
        self.root = None
