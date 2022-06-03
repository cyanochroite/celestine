import tkinter
import tkinter.ttk

class Window():
    def make(self, root, frame):
        frame.grid()
        tkinter.ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
        tkinter.ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)

    def run(self, name):
        root = tkinter.Tk(name, name, name, True, False, None)
        frame = tkinter.ttk.Frame(root, padding=10)
        self.make(root, frame)
        root.mainloop()
