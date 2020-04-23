import tkinter
import tkinter.ttk


class window():
    def __init__(self):
        self.tk = self._init_tk()
        self.button_back = self._init_button("<<", self._button_back)
        self.button_next = self._init_button(">>", self._button_next)
        self.button_quit = self._init_button("Exit Program", self.tk.quit)

        self.create_widgets()

    def _init_button(self, text, command):
        button = tkinter.Button(self.tk)
        button["text"] = text
        button["command"] = command
        return button

    def _init_tk(self):
        tk = tkinter.Tk()
        tk.title("A title")
        tk.iconbitmap("favicon.ico")
        return tk

    def create_widgets(self):
        self.button_quit = tkinter.Button(
            self.tk, text="Exit Program", command=self.tk.quit)
        self.button_quit.grid(row=0, column=1)
        #
        self.laddel = tkinter.Label()
        self.laddel.grid(row=1, column=0, columnspan=3)

        self.button_back.grid(row=2, column=0)
        self.button_next.grid(row=2, column=2)

    def reset_image(self):
        laddel["image"] = image_list.get()

    def _button_back(self):
        image_list.back()
        self.reset_image()

    def _button_next(self):
        image_list.next()
        self.reset_image()

    def mainloop(self):
        self.tk.mainloop()


app = window()
app.mainloop()
