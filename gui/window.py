import PIL

from PIL import ImageTk
from list import list


from Frame import Frame
from one import one
from two import two


class MainApplication(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.statusbar = one(self.master)
        self.left = one(self.master)
        self.two = two(self.master)

        icon1 = PIL.ImageTk.PhotoImage(PIL.Image.open("character.jpg"))
        icon2 = PIL.ImageTk.PhotoImage(PIL.Image.open("logo.jpg"))
        icon3 = PIL.ImageTk.PhotoImage(PIL.Image.open("victory.jpg"))

        image_list = list()
        image_list.add(icon1)
        image_list.add(icon2)
        image_list.add(icon3)

        self.statusbar.create_widgets(image_list)
        self.left.create_widgets(image_list)
        self.two.create_widgets(image_list)

        self.statusbar.grid(row=0, column=0)
        self.left.grid(row=1, column=0)
        self.two.grid(row=0, column=1, rowspan=2)

