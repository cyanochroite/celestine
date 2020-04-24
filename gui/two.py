from Frame import Frame


class two(Frame):
    def __init__(self, data, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.data = data
        self.image_list = data.image_list
        #
        self.icon = []

        for index in range(0, self.image_list._max + 1):
            get = self.image_list._list[index]
            image = self._init_label(get, 128, 128)
            image.grid(row=index, column=0)
            self.icon.append(image)

    def reset_image(self):
        self.label_screen["image"] = self.image_list.get()

    def _button_back(self):
        self.image_list.back()
        self.reset_image()

    def _button_next(self):
        self.image_list.next()
        self.reset_image()

    def draw(self):
        pass

    def make(self):
        pass
