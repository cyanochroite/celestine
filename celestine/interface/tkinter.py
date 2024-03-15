""""""

from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.typed import (
    A,
    H,
    N,
    S,
    R,
    override,
)
from celestine.window.collection import Area


class Element(Element_):
    """"""

    @override
    def make(self, canvas: A) -> N:
        """"""
        tkinter = self.hold.package.tkinter

        def callback() -> N:
            """"""
            self.click(self.area.local.centroid)
            self.hold.dequeue()

        if self.action or self.goto:
            self.canvas = tkinter.Button(
                canvas,
                command=callback,
                text=self.text,
            )
        else:
            self.canvas = tkinter.Label(
                canvas,
                fg="blue",
                height=4,
                text=self.text,
                width=100,
            )

        dot_x, dot_y = self.area.local.origin.int
        width, height = self.area.local.size
        self.canvas.place(
            x=dot_x,
            y=dot_y,
            width=width,
            height=height,
        )

        super().make(canvas)

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        if self.keep:
            # check may be removed if view has object
            self.keep.place_forget()

    @override
    def show(self) -> N:
        """"""
        super().show()
        if self.keep:
            # check may be removed if view has object
            # also this mostly calling render()
            width, height = self.area.local.size
            dot_x, dot_y = self.area.local.origin.int
            self.keep.place(
                x=dot_x,
                y=dot_y,
                width=width,
                height=height,
            )


class View(View_):
    """"""

    @override
    def make(self, canvas: A) -> N:
        """"""
        tkinter = self.hold.package.tkinter

        self.canvas = tkinter.Frame(
            canvas,
            padx=5,
            pady=5,
            bg="yellow",
            width=1920,
            height=1080,
        )
        dot_x, dot_y = self.area.local.origin.int
        self.canvas.place(x=dot_x, y=dot_y)

        super().make(self.canvas)

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        for _, item in self:
            item.hide()

    @override
    def show(self) -> N:
        """"""
        super().show()
        for _, item in self:
            item.show()


class Window(Window_):
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
    def make(self) -> N:
        """"""
        tkinter = self.hold.package.tkinter

        self.canvas = tkinter.Tk()
        self.canvas.title(self.hold.language.APPLICATION_TITLE)
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
    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        self.canvas.mainloop()
        return False

    @override
    def __init__(self, hold: H, **star: R) -> N:
        element = {
            "element": Element,
            "view": View,
            "window": self,
        }
        super().__init__(hold, element, **star)
        self.area = Area.make(1280, 1080)
