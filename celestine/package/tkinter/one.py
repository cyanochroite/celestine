from package.tkinter.Widget import Frame


class one(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

    def _make(self):
        self.button_back = self.Button(text="<<", command=self._button_back)
        self.button_next = self.Button(text=">>", command=self._button_next)
        self.button_quit = self.Button(
            text="Exit Program", command=self.tk.quit)
        self.label_screen = self.Label(
            image=self.data.list_get(), width=512, height=512)

    def _show(self):
        self.button_quit.grid(row=0, column=1)
        self.button_back.grid(row=2, column=0)
        self.button_next.grid(row=2, column=2)
        self.label_screen.grid(row=1, column=0, columnspan=3)

    def reset_image(self):
        self.label_screen["image"] = self.data.list_get()

    def _button_back(self):
        self.data.list_back()
        self.reset_image()

    def _button_next(self):
        self.data.list_next()
        self.reset_image()
