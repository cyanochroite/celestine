""""""

from celestine.window.window import Window as window

from . import package


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

    def __init__(self, session, element, size, **star):
        super().__init__(session, element, size, **star)
        self.root = None
