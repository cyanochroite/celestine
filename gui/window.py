from application import application


class window(application):
    def __init__(self, image_list):
        super().__init__(image_list)

        self.button_back = self._init_button("<<", self._button_back)
        self.button_next = self._init_button(">>", self._button_next)
        self.button_quit = self._init_button("Exit Program", self.tk.quit)
        self.label_screen = self._init_label(self.image_list.get())

        self.create_widgets()

    def create_widgets(self):
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
