import tkinter as tk


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(
            self.frame, text='New Window', width=25, command=self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(
            self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()


if __name__ == '__main__':
    main()
    win1 = tk.Tk()
    win2 = tk.Tk()

    tk.Button(win1, text='Button 1', command=win1.destroy).pack()
    tk.Button(win2, text='Button 2', command=win2.destroy).pack()
    win1.mainloop()

