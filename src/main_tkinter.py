from package.tkinter.Widget import Tk
from package.tkinter.window import Window
from window import WindowModel
root = Tk()
model = WindowModel()
window = Window(root, data=model)
window.grid(row=0, column=0)
root.mainloop()
