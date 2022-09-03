import tkinter as tk
from tkinter import ttk


import tkinter
import tkinter.ttk


def show_frame(cont):
    global frames
    global container

    frame = frames[cont]
    frame = frame(container)
    frame.grid(row=0, column=0, sticky="nsew")

    frame.tkraise()


LARGEFONT = ("Verdana", 35)


class StartPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        frame = tkinter.Frame(parent)

        frame = self

        # label of frame Layout 2
        label = ttk.Label(frame, text="Startpage", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(frame, text="Page 1",
                             command=lambda: show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text layout2
        button2 = ttk.Button(frame, text="Page 2",
                             command=lambda: show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent):

        tk.Frame.__init__(self, parent)

        frame = tkinter.Frame(parent)

        frame = self

        label = ttk.Label(frame, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(frame, text="StartPage",
                             command=lambda: show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(frame, text="Page 2",
                             command=lambda: show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        frame = tkinter.Frame(parent)

        frame = self

        label = ttk.Label(frame, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(frame, text="Page 1",
                             command=lambda: show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(frame, text="Startpage",
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
    frames[F] = F

show_frame(StartPage)


# session.window.setup(session)
# session.window.view(session)

root.mainloop()


from tkinter import *


def show_frame(cont):
    global frames
    global container

    frame = frames[cont]
    frame.grid(row=0, column=0, sticky="nsew")

    frame.tkraise()


ws = Tk()
ws.title('Python Guides')
ws.geometry('650x600')


container = tk.Frame(ws)
container.pack(side="top", fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)



frame0 = Frame(container, padx=5, pady=5)
#frame0.grid(row=0, column=1)

frame1 = Frame(container, padx=5, pady=5)
#frame1.grid(row=0, column=1)

frame2 = Frame(container, padx=5, pady=5)
#frame2.grid(row=0, column=1)


frame = frame0
# StartPage
label = ttk.Label(frame, text="Startpage", font=LARGEFONT)
label.pack()
#label.grid(row=0, column=4, padx=10, pady=10)

button1 = ttk.Button(frame, text="Page 1", command=lambda: show_frame(Page1))
button1.pack()
#button1.grid(row=1, column=1, padx=10, pady=10)

button2 = ttk.Button(frame, text="Page 2", command=lambda: show_frame(Page2))
button2.pack()
#button2.grid(row=2, column=1, padx=10, pady=10)


frame = frame1
# Page1
label = ttk.Label(frame, text="Page 1", font=LARGEFONT)
label.pack()
#label.grid(row=0, column=4, padx=10, pady=10)

button1 = ttk.Button(frame, text="StartPage", command=lambda: show_frame(StartPage))
button1.pack()
#button1.grid(row=1, column=1, padx=10, pady=10)

button2 = ttk.Button(frame, text="Page 2", command=lambda: show_frame(Page2))
button2.pack()
#button2.grid(row=2, column=1, padx=10, pady=10)

frame = frame2
# Page2
label = ttk.Label(frame, text="Page 2", font=LARGEFONT)
label.pack()
#label.grid(row=0, column=4, padx=10, pady=10)

button1 = ttk.Button(frame, text="Page 1", command=lambda: show_frame(Page1))
button1.pack()
#button1.grid(row=1, column=1, padx=10, pady=10)

button2 = ttk.Button(frame, text="Startpage", command=lambda: show_frame(StartPage))
button2.pack()
#button2.grid(row=2, column=1, padx=10, pady=10)



frames = {}
frames[StartPage] = frame0
frames[Page1] = frame1
frames[Page2] = frame2

show_frame(StartPage)

ws.mainloop()
