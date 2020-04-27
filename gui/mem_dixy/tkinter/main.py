import tkinter
import tkinter.ttk
import mem_dixy.tkinter.window
import mem_dixy.window

root = tkinter.Tk()
model = mem_dixy.window.WindowModel()
window = mem_dixy.tkinter.window.MainApplication(
    root,
    data=model
)
window.grid(row=0, column=0)
root.mainloop()
