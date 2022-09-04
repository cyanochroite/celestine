import tkinter
from tkinter import filedialog as tkfd
from PIL import Image
from PIL import ImageTk

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
phat_list = []
images_reference_list = []


def find_photos():
    photo = tkfd.askopenfile()

    file_path = photo.name
    img = Image.open(file_path)
    photo_image = ImageTk.PhotoImage(img)
    tkinter.Label(window, image=photo_image).pack(side=tkinter.TOP)
    images_reference_list.append(photo_image)

    phat_list.append(file_path)


window = tkinter.Tk()
canvas = tkinter.Frame(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="green")
canvas.pack(side=tkinter.BOTTOM)

b1 = tkinter.Button(canvas, text="Click me to add 5 photos of yourself", height=5, width=30, command=find_photos)
b1.pack()


window.mainloop()
