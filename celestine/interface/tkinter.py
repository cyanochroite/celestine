""""""

from celestine import load
from celestine.package import tkinter
from celestine.window.element import Abstract as Abstract_
from celestine.window.element import Button as Button_
from celestine.window.element import Image as Image_
from celestine.window.element import Label as Label_
from celestine.window.window import Window as window


class Abstract(Abstract_):
    """"""

    def render(self, view, item, **star):
        """"""
        self.item = item(view, **star)

        width = self.x_max - self.x_min
        height = self.y_max - self.y_min
        self.item.place(
            x=self.x_min,
            y=self.y_min,
            width=width,
            height=height,
        )


class Button(Abstract, Button_):
    """"""

    def callback(self):
        """"""
        self.call(self.action, **self.argument)

    def draw(self, view, *, make, **star):
        """"""

        if not make:
            return

        item = tkinter.Button
        star.update(command=self.callback)
        star.update(text=f"button:{self.data}")
        self.render(view, item, **star)


class Image(Abstract, Image_):
    """"""

    def draw(self, view, *, make, **star):
        """"""
        file = self.image or load.pathway.asset("null.png")

        if not make:
            return

        item = tkinter.Label
        self.cache = tkinter.PhotoImage(file=file)
        star.update(image=self.cache)
        self.render(view, item, **star)

    def update(self, *, image, **star):
        """"""
        if not super().update(image=image, **star):
            return False

        self.cache = tkinter.PhotoImage(file=self.image)
        self.item.configure(image=self.cache)
        self.item.image = self.cache
        return True


class Label(Abstract, Label_):
    """"""

    def draw(self, view, *, make, **star):
        """"""
        if not make:
            return

        item = tkinter.Label
        star.update(fg="blue")
        star.update(height=4)
        star.update(text=f"label:{self.data}")
        star.update(width=100)
        self.render(view, item, **star)


class Window(window):
    """"""

    def data(self, container):
        """"""
        container.data = tkinter.Frame(
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
        self.root = tkinter.Tk()
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


def image_format():
    """"""
    return [
        ".pbm",
        ".pgm",
        ".ppm",
        ".pnm",
        ".gif",
        ".png",
    ]


def window(session, **star):
    """"""
    element = {
        "button": Button,
        "image": Image,
        "label": Label,
    }
    size = (1280, 1080)
    return Window(session, element, size, **star)
