from mem_dixy.package.tkinter.Widget import Tk
from mem_dixy.package.tkinter.window import Window
from mem_dixy.window import WindowModel
root = Tk()
model = WindowModel()
window = Window(root, data=model)
window.grid(row=0, column=0)
root.mainloop()
