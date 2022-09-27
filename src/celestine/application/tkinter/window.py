from celestine.package import tkinter
from celestine.application.tkinter.page import Page
from celestine.application.window import Window as Window_


class Window(Window_):

    def page(self):
        return Page(self)

    def __enter__(self):
        self.root = tkinter.Tk()
        self.root.title(self.session.language.APPLICATION_TITLE)

        self.root.geometry("1920x1080")
        self.root.minsize(640, 480)
        self.root.maxsize(3840, 2160)
        self.root.config(bg="blue")
        return self

    def __exit__(self, *_):
        self.root.mainloop()
        return False

    def __getitem__(self, key):
        frame = self.frame_get(key)
        frame.tkraise()

    def __init__(self, session):
        super().__init__(session)
        self.root = None
