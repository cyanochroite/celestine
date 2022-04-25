from tkinter import *
import functools

root = Tk()
root.title("Simple Calculator")

display = Entry(root, width=36, borderwidth=8)
display.grid(row=0, column=0, columnspan=3, padx=8, pady=8)

storage = 0
register = 0


def button_click(number):
    append = display.get()
    display.delete(0, END)
    global register
    register = append + number
    display.insert(0, register)
    return


def button_add():
    display.delete(0, END)
    global storage
    global register
    storage += int(register)
    return


def button_equal():
    display.delete(0, END)
    global storage
    global register
    storage += int(register)
    display.insert(0, storage)


def button_clear():
    display.delete(0, END)


def make_button(text):
    return Button(root, text=text, padx=40, pady=20, command=functools.partial(button_click, text))


button_0 = make_button("0")
button_1 = make_button("1")
button_2 = make_button("2")
button_3 = make_button("3")
button_4 = make_button("4")
button_5 = make_button("5")
button_6 = make_button("6")
button_7 = make_button("7")
button_8 = make_button("8")
button_9 = make_button("9")
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=71,
                      pady=20, command=button_clear)

button_0.grid(row=4, column=0)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()
