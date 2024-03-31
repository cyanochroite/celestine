""""""

from celestine import bank
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.typed import (
    A,
    B,
    N,
    R,
    S,
    override,
)
from celestine.window.collection import Area


class Abstract(Abstract_):
    """"""

    def place(self, item: A) -> N:
        width, height = self.area.local.size
        dot_x, dot_y = self.area.local.origin.int
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
        tkinter = bank.package.tkinter

        def callback() -> N:
            """"""
            self.click(self.area.world.centroid)
            bank.dequeue()

        if self.action or self.goto:
            self.item = tkinter.Button(
                canvas,
                command=callback,
                text=self.text,
            )
        else:
            self.item = tkinter.Label(
                canvas,
                fg="blue",
                height=4,
                text=self.text,
                width=100,
            )

        self.place(self.item)
        super().make(canvas)

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
        tkinter = bank.package.tkinter

        self.canvas = tkinter.Frame(
            canvas,
            padx=5,
            pady=5,
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
    def extension(self):
        """"""
        if bank.package.pillow:
            return bank.package.pillow.extension()

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
        tkinter = bank.package.tkinter

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
