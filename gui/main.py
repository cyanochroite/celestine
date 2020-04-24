import tkinter
import tkinter.ttk

from window import MainApplication


if __name__ == "__main__":
    root = tkinter.Tk()
    MainApplication(root).grid(row=0, column=0)
    root.mainloop()
