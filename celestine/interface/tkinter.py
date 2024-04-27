""""""

from celestine import bank
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.package import (
    pillow,
    tkinter,
)
from celestine.typed import (
    A,
    B,
    LS,
    N,
    R,
    S,
    P,
    override,
)
from celestine.window.collection import Area


class Abstract(Abstract_):
    """"""

    def place(self, item: A) -> N:
        """"""
        width, height = self.area.local.size
        dot_x, dot_y = self.area.local.origin
        item.place(
            x=dot_x,
            y=dot_y,
            width=width,
            height=height,
        )


class Element(Element_, Abstract):
    """"""

    @override
    def make(self, canvas: A) -> N:
        """"""

        super().make(canvas)

        def callback() -> N:
            """"""
            self.click(self.area.world.centroid)
            bank.dequeue()

        star: R = {}
        # if not super().make(canvas):
        #    return False

        # if not super().draw(**star):
        #    return False

        if self.path:
            self.image2 = tkinter.PhotoImage(file=self.path)
            star.update(image=self.image2)

        if self.text:
            star.update(text=self.text)

        if self.action or self.goto:
            star.update(command=callback)
            self.item = tkinter.Button(canvas, **star)
        else:
            star.update(fg="blue")
            star.update(height=4)
            star.update(text=self.text)
            star.update(width=100)
            self.item = tkinter.Label(canvas, **star)

        self.place(self.item)

    def update(self, path: P, **star: R) -> N:
        """"""
        super().update(path)

        if pillow:
            image = self.image.image
            self.image2 = pillow.ImageTk.PhotoImage(image=image)
        else:
            # breaks other stuff elsewere
            self.image2 = tkinter.PhotoImage(file=self.path)

        self.item.configure(image=self.image2)
        self.item.image = self.image2

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        self.item.place_forget()

    @override
    def show(self) -> N:
        """"""
        super().show()
        self.place(self.item)


class View(View_, Abstract):
    """"""

    @override
    def make(self, canvas: A) -> N:
        """"""
        self.canvas = tkinter.Frame(
            canvas,
            padx=0,
            pady=0,
            bg="yellow",
            width=1920,
            height=1080,
        )
        self.place(self.canvas)
        super().make(self.canvas)

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        self.canvas.place_forget()

    @override
    def show(self) -> N:
        """"""
        super().show()
        self.place(self.canvas)


class Window(Window_):
    """"""

    @override
    def extension(self) -> LS:
        """"""
        if pillow:
            return pillow.extension()

        return [
            ".pbm",
            ".pgm",
            ".ppm",
            ".pnm",
            ".gif",
            ".png",
        ]

    @override
    def make(self) -> N:
        """"""
        self.canvas = tkinter.Tk()
        self.canvas.title(bank.language.APPLICATION_TITLE)
        self.canvas.geometry("1920x1080")
        self.canvas.minsize(640, 480)
        self.canvas.maxsize(3840, 2160)
        self.canvas.config(bg="blue")

        super().make()

    @override
    def turn(self, page: S, **star: R) -> N:
        super().turn(page, **star)
        self.page.canvas.tkraise()

    @override
    def __exit__(self, exc_type: A, exc_value: A, traceback: A) -> B:
        super().__exit__(exc_type, exc_value, traceback)
        self.canvas.mainloop()
        return False

    @override
    def __init__(self, **star: R) -> N:
        element = {
            "element": Element,
            "view": View,
            "window": self,
        }
        super().__init__(element, **star)
        self.area = Area.make(1280, 1080)
