""""""


from celestine.typed import (
    CA,
    N,
    P,
    R,
    S,
)
from celestine.window.collection import Rectangle
from celestine.window.element import Abstract as Abstract_
from celestine.window.element import Button as Button_
from celestine.window.element import Image as Image_
from celestine.window.element import Label as Label_
from celestine.window.window import Window as Window_


class Abstract(Abstract_):
    """"""

    def render(self, item: CA, *, ring: R, **star) -> N:
        """"""
        self.item = item(self.canvas, **star)

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

    def callback(self) -> N:
        """"""
        self.call(self.action, **self.argument)

    def make(self, ring: R, **star) -> N:
        """"""
        tkinter = ring.package.tkinter

        item = tkinter.Button
        star.update(command=self.callback)
        star.update(text=f"button:{self.data}")
        self.render(item, ring=ring, **star)


class Image(Abstract, Image_):
    """"""

    def make(self, ring: R, **star) -> N:
        """"""
        tkinter = ring.package.tkinter

        self.image = tkinter.PhotoImage(file=self.path)
        star.update(image=self.image)

        item = tkinter.Label
        self.render(item, ring=ring, **star)

    def update(self, ring: R, path: P, **star) -> N:
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


class Label(Abstract, Label_):
    """"""

    def make(self, ring: R, **star) -> N:
        """"""
        tkinter = ring.package.tkinter

        item = tkinter.Label
        star.update(fg="blue")
        star.update(height=4)
        star.update(text=f"label:{self.data}")
        star.update(width=100)
        self.render(item, ring=ring, **star)


class Window(Window_):
    """"""

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

    def setup(self, name: S) -> N:
        """"""
        tkinter = self.ring.package.tkinter

        canvas = tkinter.Frame(
            self.canvas,
            padx=5,
            pady=5,
            bg="skyblue",
            width=1920,
            height=1080,
        )
        canvas.place(x=0, y=0)
        return canvas

    def turn(self, page, **star):
        super().turn(page, **star)
        self.page.canvas.tkraise()

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

        canvas = ring.package.tkinter.Tk()
        canvas.title(ring.language.APPLICATION_TITLE)
        canvas.geometry("1920x1080")
        canvas.minsize(640, 480)
        canvas.maxsize(3840, 2160)
        canvas.config(bg="blue")

        super().__init__(ring, canvas, element, area, **star)
