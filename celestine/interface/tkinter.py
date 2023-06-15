""""""

from celestine import load
from celestine.typed import R
from celestine.window.element import Abstract as Abstract_
from celestine.window.element import Button as Button_
from celestine.window.element import Image as Image_
from celestine.window.element import Label as Label_
from celestine.window.element import Photo as Photo_
from celestine.window.window import Window as Window_


class Abstract(Abstract_):
    """"""

    def render(self, view, item, *, ring, **star):
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

    def draw(self, ring: R, view, *, make, **star):
        """"""
        tkinter = ring.package.tkinter

        if not make:
            return

        item = tkinter.Button
        star.update(command=self.callback)
        star.update(text=f"button:{self.data}")
        self.render(view, item, ring=ring, **star)


class Image(Abstract, Image_):
    """"""

    def draw(self, ring: R, view, *, make, **star):
        """"""
        tkinter = ring.package.tkinter

        file = self.image or load.pathway.asset("null.png")

        if not make:
            return

        item = tkinter.Label
        self.cache = tkinter.PhotoImage(file=file)
        star.update(image=self.cache)
        self.render(view, item, ring=ring, **star)

    def update(self, ring: R, image, **star):
        """"""
        tkinter = ring.package.tkinter

        if not super().update(ring, image, **star):
            return False

        pillow = ring.package.pillow
        if pillow:
            self.cache = pillow.ImageTk.PhotoImage(file=self.image)
        else:
            self.cache = tkinter.PhotoImage(file=self.image)

        self.item.configure(image=self.cache)
        self.item.image = self.cache
        return True


class Label(Abstract, Label_):
    """"""

    def draw(self, ring: R, view, *, make, **star):
        """"""
        tkinter = ring.package.tkinter

        if not make:
            return

        item = tkinter.Label
        star.update(fg="blue")
        star.update(height=4)
        star.update(text=f"label:{self.data}")
        star.update(width=100)
        self.render(view, item, ring=ring, **star)


class Photo(Abstract, Photo_):
    """"""

    def draw(self, ring: R, view, *, make, **star):
        """"""
        tkinter = ring.package.tkinter

        file = self.image or load.pathway.asset("null.png")

        if not make:
            return

        item = tkinter.Label
        self.cache = tkinter.PhotoImage(file=file)
        star.update(image=self.cache)
        self.render(view, item, ring=ring, **star)

    def update(self, ring: R, image, **star):
        """"""
        tkinter = ring.package.tkinter

        if not super().update(ring, image, **star):
            return False

        pillow = ring.package.pillow
        if pillow:
            self.cache = pillow.ImageTk.PhotoImage(file=self.image)
        else:
            self.cache = tkinter.PhotoImage(file=self.image)

        self.item.configure(image=self.cache)
        self.item.image = self.cache
        return True


class Window(Window_):
    """"""

    def data(self, container):
        """"""
        tkinter = self.ring.package.tkinter

        container.data = tkinter.Frame(
            self.root,
            padx=5,
            pady=5,
            bg="skyblue",
            width=1920,
            height=1080,
        )
        container.data.place(x=0, y=0)

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
        self.page.data.tkraise()

    def __enter__(self):
        tkinter = self.ring.package.tkinter

        super().__enter__()
        self.root = tkinter.Tk()
        self.root.title(self.ring.language.APPLICATION_TITLE)
        self.root.geometry("1920x1080")
        self.root.minsize(640, 480)
        self.root.maxsize(3840, 2160)
        self.root.config(bg="blue")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        self.root.mainloop()
        return False

    def __init__(self, ring, element, size, **star):
        super().__init__(ring, element, size, **star)
        self.root = None


def window(ring, **star):
    """"""
    element = {
        "button": Button,
        "image": Image,
        "label": Label,
        "photo": Photo,
    }
    size = (1280, 1080)
    return Window(ring, element, size, **star)
