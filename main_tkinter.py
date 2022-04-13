from celestine.package.tkinter.Widget import Tk
from celestine.package.tkinter.window import Window


import os.path
import sys

from celestine.package.pillow.Image import Image
from celestine.package.pillow.ImageTk import ImageTk

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


root = Tk()
model = WindowModel()
window = Window(root, data=model)
window.grid(row=0, column=0)
root.mainloop()
