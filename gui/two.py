from Frame import Frame


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
            get = self.data.image_list._list[index]
            but = self.button(width=128, height=128, image=get)
            self.icon.append(but)

    def _show(self):
        limit = min(self.count, self.data.image_list._max + 1)
        for index in range(limit):
            row = index // self.column
            column = index % self.column
            self.icon[index].grid(row=row, column=column)
