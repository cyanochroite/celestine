from mem_dixy.tkinter.Widget import Frame

from .one import one
from .two import two


class MainApplication(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

    def _make(self):
        self.left_top = one(self.master, data=self.data)
        self.left_bottom = one(self.master, data=self.data)
        self.window = two(self.master, data=self.data)

    def _show(self):
        self.left_top.grid(row=0, column=0)
        self.left_bottom.grid(row=1, column=0)
        self.window.grid(row=0, column=1, rowspan=2)
