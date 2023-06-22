""""""

from celestine.typed import (
    A,
    N,
    R,
)
from celestine.window.collection import Rectangle
from celestine.window.element import Abstract as Abstract_
from celestine.window.element import Button as Button_
from celestine.window.element import Image as Image_
from celestine.window.element import Label as Label_
from celestine.window.window import Window as Window_


class Abstract(Abstract_):
    """"""

    def render(self, canvas, item, *, ring, **star):
        """"""
        self.item = item(canvas, **star)

        width, height = self.area.size
        dot_x, dot_y = self.area.origin
        self.item.place(
            x=dot_x,
            y=dot_y,
            width=width,
            height=height,
        )


class Button(Abstract, Button_):
    """"""

    def callback(self):
        """"""
        self.call(self.action, **self.argument)

    def make(self, ring: R, canvas: A, **star):
        """"""
        tkinter = ring.package.tkinter

        item = tkinter.Button
        star.update(command=self.callback)
        star.update(text=f"button:{self.data}")
        self.render(canvas, item, ring=ring, **star)


class Image(Abstract, Image_):
    """"""

    def make(self, ring: R, canvas: A, **star):
        """"""
        tkinter = ring.package.tkinter

        self.image = tkinter.PhotoImage(file=self.path)
        star.update(image=self.image)

        item = tkinter.Label
        self.render(canvas, item, ring=ring, **star)

    def update(self, ring: R, path, **star):
        """"""
        super().update(ring, path)
        tkinter = ring.package.tkinter
        pillow = ring.package.pillow

        if pillow:
            image = pillow.image_load(self.path)
            size = self.resize(image.size)
            image.resize(size)
            self.image = pillow.ImageTk.PhotoImage(image=image.image)
        else:
            self.image = tkinter.PhotoImage(file=self.path)

        self.item.configure(image=self.image)
        self.item.image = self.image
        return True


class Label(Abstract, Label_):
    """"""

    def make(self, ring: R, canvas: A, **star):
        """"""
        tkinter = ring.package.tkinter

        item = tkinter.Label
        star.update(fg="blue")
        star.update(height=4)
        star.update(text=f"label:{self.data}")
        star.update(width=100)
        self.render(canvas, item, ring=ring, **star)


class Window(Window_):
    """"""

    def setup(self, container):
        """"""
        tkinter = self.ring.package.tkinter

        container.canvas = tkinter.Frame(
            self.canvas,
            padx=5,
            pady=5,
            bg="skyblue",
            width=1920,
            height=1080,
        )
        container.canvas.place(x=0, y=0)

    def extension(self):
        """"""
        if self.ring.package.pillow:
            return self.ring.package.pillow.extension()

        return [
            ".pbm",
            ".pgm",
            ".ppm",
            ".pnm",
            ".gif",
            ".png",
        ]

    def turn(self, page, **star):
        super().turn(page, **star)
        self.page.canvas.tkraise()

    def __enter__(self):
        tkinter = self.ring.package.tkinter

        super().__enter__()
        self.canvas = tkinter.Tk()
        self.canvas.title(self.ring.language.APPLICATION_TITLE)
        self.canvas.geometry("1920x1080")
        self.canvas.minsize(640, 480)
        self.canvas.maxsize(3840, 2160)
        self.canvas.config(bg="blue")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        self.canvas.mainloop()
        return False

    def __init__(self, ring: R, **star) -> N:
        element = {
            "button": Button,
            "image": Image,
            "label": Label,
        }
        area = Rectangle(0, 0, 1280, 1080)
        super().__init__(ring, element, area, **star)
