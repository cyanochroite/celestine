import tkinter
import tkinter.ttk


class window():
    # class window(tkinter.Frame):
    #    def __init__(self, master=None):
    #        super().__init__(master)
    #        self.master = master
    def __init__(self):
        self.tk = tkinter.Tk()
        tk = tkinter.Tk()
        tk.title("A title")
        tk.iconbitmap("favicon.ico")

        self.create_widgets()

    def mainloop(self):
        self.tk.mainloop()

    def create_widgets(self):
        self.button_quit = tkinter.Button(
            self.tk, text="Exit Program", command=self.tk.quit)
        self.button_quit.grid(row=0, column=1)
        #
        self.laddel = tkinter.Label()
        self.laddel.grid(row=1, column=0, columnspan=3)
        #
        self.back_button = tkinter.Button(
            self.tk, text="<<", command=self.back)
        self.button_forward = tkinter.Button(
            self.tk, text=">>", command=self.forward)
        self.back_button.grid(row=2, column=0)
        self.button_forward.grid(row=2, column=2)

    def reset_image(self):
        laddel["image"] = image_list.get()

    def forward(self):
        image_list.next()
        self.reset_image()

    def back(self):
        image_list.back()
        self.reset_image()


app = window()
app.mainloop()
