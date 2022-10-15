from celestine.package.master.window import Window as master

from . import package
from .page import Page


class Window(master):
    def page(self, document):
        return Page(self, document)

    def turn(self, page):
        frame = self.frame_get(page)
        frame.tkraise()

    def __enter__(self):
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

    def __init__(self, session):
        super().__init__(session)
        self.root = None
