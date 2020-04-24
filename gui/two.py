from Frame import Frame


class two(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        self.data = kw.pop("data", None)
        self.image_list = self.data.image_list
        super().__init__(master, cnf, **kw)

    def _make(self):
        self.icon = []
        for index in range(0, self.image_list._max + 1):
            get = self.image_list._list[index]
            image = self._init_label(get, 128, 128)
            image.grid(row=index, column=0)
            self.icon.append(image)

    def _show(self):
        pass

    def reset_image(self):
        self.label_screen["image"] = self.image_list.get()

    def _button_back(self):
        self.image_list.back()
        self.reset_image()

    def _button_next(self):
        self.image_list.next()
        self.reset_image()

