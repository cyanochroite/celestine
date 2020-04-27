from mem_dixy.Pillow.ImageTk import PhotoImage
from mem_dixy.list import list


class WindowModel():
    def __init__(self):
        self._init_image_list()

    def _init_image_list(self):
        icon1 = PhotoImage("character.jpg")
        icon2 = PhotoImage("logo.jpg")
        icon3 = PhotoImage("victory.jpg")
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

    def reset_image(self):
        self.label_screen["image"] = self.image_list.get()

    def list_get(self):
        return self.image_list.get()

    def list_back(self):
        self.image_list.back()

    def list_next(self):
        self.image_list.next()

    def image_count():
        return self.image_list._max + 1

