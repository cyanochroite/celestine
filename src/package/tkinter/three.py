import functools

from package.tkinter.Widget import Frame


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
