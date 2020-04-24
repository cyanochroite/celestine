from Frame import Frame


class two(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.icon = []

    def _make(self):
        for index in range(0, self.data.image_list._max + 1):
            get = self.data.image_list._list[index]
            image = self._init_label(get, 128, 128)
            image.grid(row=index, column=0)
            self.icon.append(image)

    def _show(self):
        for index in range(0, self.data.image_list._max + 1):
            get = self.data.image_list._list[index]
            image = self._init_label(get, 128, 128)
            image.grid(row=index, column=0)
            self.icon.append(image)
