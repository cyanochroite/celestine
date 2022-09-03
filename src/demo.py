import tkinter as tk
from tkinter import ttk


import tkinter
import tkinter.ttk


def show_frame(cont):
    global frames
    frame = frames[cont]
    frame.tkraise()


LARGEFONT = ("Verdana", 35)


class StartPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Startpage", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Driver Code
root = tkinter.Tk()
root.title("session.language.APPLICATION_TITLE")

root.geometry("1920x1080")
root.minsize(640, 480)
root.maxsize(3840, 2160)
root.config(bg="skyblue")


container = tk.Frame(root)
container.pack(side="top", fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# initializing frames to an empty array
frames = {}

# iterating through a tuple consisting
# of the different page layouts
for F in (StartPage, Page1, Page2):

    frame = F(container)

    # initializing frame of that object from
    # startpage, page1, page2 respectively with
    # for loop
    frames[F] = frame

    frame.grid(row=0, column=0, sticky="nsew")

show_frame(StartPage)


# session.window.setup(session)
# session.window.view(session)

root.mainloop()
