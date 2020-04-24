import PIL

from PIL import ImageTk
from list import list


from Frame import Frame
from one import one
from two import two


class MainApplication(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        self.data = WindowModel()
        super().__init__(master, cnf, **kw)

    def draw(self):
        self.left_top.grid(row=0, column=0)
        self.left_bottom.grid(row=1, column=0)
        self.right.grid(row=0, column=1, rowspan=2)

    def make(self):
        self.left_top = one(self.data, self.master)
        self.left_bottom = one(self.data, self.master)
        self.right = two(self.data, self.master)


class WindowModel():
    def __init__(self):
        self._init_image_list()

    def _init_image_list(self):
        icon1 = PIL.ImageTk.PhotoImage(PIL.Image.open("character.jpg"))
        icon2 = PIL.ImageTk.PhotoImage(PIL.Image.open("logo.jpg"))
        icon3 = PIL.ImageTk.PhotoImage(PIL.Image.open("victory.jpg"))
        image_list = list()
        image_list.add(icon1)
        image_list.add(icon2)
        image_list.add(icon3)
        self.image_list = image_list
