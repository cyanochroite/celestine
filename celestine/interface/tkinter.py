""""""


from celestine.interface import Abstract as Abstract_
from celestine.interface import Button as Button_
from celestine.interface import Image as Image_
from celestine.interface import Label as Label_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.typed import (
    C,
    H,
    N,
    P,
    R,
    S,
    override,
)
from celestine.window.collection import Plane


class Abstract(Abstract_):
    """"""

    def render(self, keep: C, **star: R) -> N:
        """"""
        self.keep = keep(self.canvas, **star)

        width, height = self.area.size
        dot_x, dot_y = self.area.origin.int
        self.keep.place(
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

    def make(self) -> N:
        """"""
        tkinter = self.hold.package.tkinter

        keep = tkinter.Button
        self.render(
            keep,
            command=self.callback,
            text=f"button: {self.data}",
        )


class Image(Abstract, Image_):
    """"""

    def make(self) -> N:
        """"""
        tkinter = self.hold.package.tkinter
        self.render(
            tkinter.Label,
            image=self.image.image,
        )

    @override
    def update(self, path: P, **star: R) -> N:
        """"""
        super().update(path)
        tkinter = self.hold.package.tkinter
        pillow = self.hold.package.pillow

        if pillow:
            image = pillow.open(self.path)
            size = self.resize(image.size)
            image.resize(size)
            self.image = pillow.ImageTk.PhotoImage(image=image.image)
        else:
            self.image = tkinter.PhotoImage(file=self.path)

        self.keep.configure(image=self.image)
        self.keep.image = self.image


class Label(Abstract, Label_):
    """"""

    def make(self) -> N:
        """"""
        tkinter = self.hold.package.tkinter

        keep = tkinter.Label
        self.render(
            keep,
            fg="blue",
            height=4,
            text=f"label:{self.data}",
            width=100,
        )


class View(Abstract, View_):
    """"""


class Window(Abstract, Window_):
    """"""

    @override
    def extension(self):
        """"""
        if self.hold.package.pillow:
            return self.hold.package.pillow.extension()

        return [
            ".pbm",
            ".pgm",
            ".ppm",
            ".pnm",
            ".gif",
            ".png",
        ]

    @override
    def setup(self, name: S) -> N:
        """"""
        tkinter = self.hold.package.tkinter

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

    @override
    def turn(self, page):
        super().turn(page)
        self.page.canvas.tkraise()

    @override
    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        self.canvas.mainloop()
        return False

    @override
    def __init__(self, hold: H, **star: R) -> N:
        element = {
            "button": Button,
            "image": Image,
            "label": Label,
        }

        canvas = hold.package.tkinter.Tk()
        canvas.title(hold.language.APPLICATION_TITLE)
        canvas.geometry("1920x1080")
        canvas.minsize(640, 480)
        canvas.maxsize(3840, 2160)
        canvas.config(bg="blue")

        super().__init__(hold, canvas, element, **star)
        self.area = Plane.make(1280, 1080)
