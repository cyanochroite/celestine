from Frame import Frame
import functools


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
                self.button(
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
