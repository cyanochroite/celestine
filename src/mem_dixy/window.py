import os.path
import sys

from mem_dixy.package.pillow.Image import Image
from mem_dixy.package.pillow.ImageTk import ImageTk
from mem_dixy.list import list


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
