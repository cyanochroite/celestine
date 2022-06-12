import tkinter
import tkinter.ttk
import functools
import abc
import os.path
import sys

from celestine.package.pillow.Image import Image
from celestine.package.pillow.ImageTk import ImageTk


class Frame(tkinter.Frame, metaclass=abc.ABCMeta):
    def __init__(self, master=None, cnf={}, **kw):
        self.data = kw.pop("data", None)
        super().__init__(master, cnf, **kw)
        self.master = self
        self._make()
        self._show()
        self.END = tkinter.END

    @abc.abstractmethod
    def _make(self):
        pass

    @abc.abstractmethod
    def _show(self):
        pass

    def Button(self, **kw):
        return tkinter.Button(self.master, **kw)

    def Entry(self, **kw):
        return tkinter.Entry(self.master, **kw)

    def Label(self, **kw):
        return tkinter.Label(self.master, **kw)

    def Text(self, **kw):
        return tkinter.Text(self.master, **kw)

    def StringVar(self, **kw):
        return tkinter.StringVar()


class one(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

    def _make(self):
        self.button_back = self.Button(text="<<", command=self._button_back)
        self.button_next = self.Button(text=">>", command=self._button_next)
        self.button_quit = self.Button(
            text="Exit Program", command=self.tk.quit)
        self.label_screen = self.Label(
            image=self.data.list_get(), width=512, height=512)

    def _show(self):
        self.button_quit.grid(row=0, column=1)
        self.button_back.grid(row=2, column=0)
        self.button_next.grid(row=2, column=2)
        self.label_screen.grid(row=1, column=0, columnspan=3)

    def reset_image(self):
        self.label_screen["image"] = self.data.list_get()

    def _button_back(self):
        self.data.list_back()
        self.reset_image()

    def _button_next(self):
        self.data.list_next()
        self.reset_image()


class two(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        self.row = 3
        self.column = 4
        self.count = self.row * self.column
        super().__init__(master, cnf, **kw)

    def _make(self):
        self.icon = []
        limit = min(self.count, self.data.image_list._max + 1)
        for index in range(limit):
            self.icon.append(
                self.Button(
                    command=functools.partial(self.hippo, index),
                    height=128,
                    image=self.data.image_list._list[index],
                    width=128
                )
            )

    def _show(self):
        limit = min(self.count, self.data.image_list._max + 1)
        for index in range(limit):
            row = index // self.column
            column = index % self.column
            self.icon[index].grid(row=row, column=column)

    def hippo(self, index):
        print(index)


class three(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        self.row = 3
        self.column = 4
        self.count = self.row * self.column
        super().__init__(master, cnf, **kw)

    def _make(self):
        self.word = self.Text(height=8, width=128)
        self.username = self.StringVar()
        self.name = self.Entry(textvariable=self.username)
        self.push = self.Button(text="<<", command=self._button_submit)

    def _show(self):
        self.word.grid(row=0, column=0)
        self.name.grid(row=1, column=0)
        self.push.grid(row=2, column=0)

    def _button_submit(self):
        self.word.insert(self.END, self.username.get())


class my_window(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

    def _make(self):
        self.left_top = one(self.master, data=self.data)
        self.left_bottom = one(self.master, data=self.data)
        self.window = two(self.master, data=self.data)
        self.bottom = three(self.master, data=self.data)

    def _show(self):
        self.left_top.grid(row=0, column=0)
        self.left_bottom.grid(row=1, column=0)
        self.window.grid(row=0, column=1, rowspan=2)
        self.bottom.grid(row=2, column=0, columnspan=2)


def Tk():
    return tkinter.Tk()


class list:
    def __init__(self):
        self._list = []
        self._index = 0
        self._min = 0
        self._max = -1

    def add(self, item):
        self._list.append(item)
        self._max += 1

    def back(self):
        if self._index > self._min:
            self._index -= 1

    def get(self):
        return self._list[self._index]

    def next(self):
        if self._index < self._max:
            self._index += 1

    def reset(self):
        self._index = self._min


class WindowModel():
    def __init__(self):
        self._init_image_list()

    def _init_image_list(self):
        path = self.get_path()
        path = "D:/file/"
        icon1 = self._load_image(path, "character.jpg")
        icon2 = self._load_image(path, "logo.jpg")
        icon3 = self._load_image(path, "victory.jpg")
        image_list = list()
        image_list.add(icon1)
        image_list.add(icon1)
        image_list.add(icon1)
        image_list.add(icon1)
        image_list.add(icon2)
        image_list.add(icon2)
        image_list.add(icon2)
        image_list.add(icon2)
        image_list.add(icon3)
        image_list.add(icon3)
        image_list.add(icon3)
        image_list.add(icon3)
        self.image_list = image_list

    def _load_image(self, path, name):
        file = os.path.join(path, name)
        image = Image.open(file)
        photo = ImageTk.PhotoImage(image.image)
        return photo

    def reset_image(self):
        self.label_screen["image"] = self.image_list.get()

    def list_get(self):
        return self.image_list.get()

    def list_back(self):
        self.image_list.back()

    def list_next(self):
        self.image_list.next()

    def image_count(self):
        return self.image_list._max + 1

    def get_path(self):
        argv = sys.argv
        path = argv[0]
        path = os.path.normcase(path)
        path = os.path.normpath(path)
        path = os.path.abspath(path)
        path = os.path.dirname(path)
        path = os.path.join(path, "file")
        return path


import tkinter

class Image():
    def load(cls, file):
        return cls(tkinter.PhotoImage(file=file))

    def __init__(self, image):
        self.height = image.height()
        self.image = image
        self.width = image.width()

    @classmethod
    def load(cls, file):
        cls()


class Window():
    def __init__(self):
        self.image = []

    def label_add(self, image):
        tkinter.Label(self.root, image=image).pack()

    def image_load(self, file):
        image = tkinter.PhotoImage(file=file)
        self.image.append(image)
        return image

    def run(self, call):
        self.root = tkinter.Tk()
        self.root.title('celestine · PyPI')

        self.root.geometry("900x550") # Set the starting size of the window
        self.root.maxsize(900, 600) # width x height
        self.root.config(bg="skyblue")
        
        
        call(self)
        
        image = self.image_load("D:\\file\\anitest.gif")
        self.label_add(image)
#        tkinter.Label(self.root, image=image).pack()
        self.root.mainloop()

