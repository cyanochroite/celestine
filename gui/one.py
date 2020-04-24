from Frame import Frame


class one(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        self.data = kw.pop("data", None)
        self.image_list = self.data.image_list
        super().__init__(master, cnf, **kw)

    def _make(self):
        self.button_back = self._init_button("<<", self._button_back)
        self.button_next = self._init_button(">>", self._button_next)
        self.button_quit = self._init_button("Exit Program", self.tk.quit)
        self.label_screen = self._init_label(self.image_list.get(), 512, 512)

    def _show(self):
        self.button_quit.grid(row=0, column=1)
        self.button_back.grid(row=2, column=0)
        self.button_next.grid(row=2, column=2)
        self.label_screen.grid(row=1, column=0, columnspan=3)

    def reset_image(self):
        self.label_screen["image"] = self.image_list.get()

    def _button_back(self):
        self.image_list.back()
        self.reset_image()

    def _button_next(self):
        self.image_list.next()
        self.reset_image()
