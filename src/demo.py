import tkinter as tk
from tkinter import filedialog as tkfd
from PIL import ImageTk, Image
import time
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
phat_list = []
images_reference_list = []


def find_photos():
    photo = tkfd.askopenfile()

    file_path = photo.name
    img = Image.open(file_path)
    photo_image = ImageTk.PhotoImage(img)
    tk.Label(window, image=photo_image).pack(side=tk.TOP)
    images_reference_list.append(photo_image)

    phat_list.append(file_path)


window = tk.Tk()
# creates the canvas
canvas = tk.Canvas(window, width=WINDOW_WIDTH,
                   height=WINDOW_HEIGHT, bg="green")
canvas.pack(side=tk.BOTTOM)

b1 = tk.Button(canvas, text="Click me to add 5 photos of yourself",
               height=5, width=30, command=find_photos)
canvas.create_window(WINDOW_WIDTH // 3, WINDOW_HEIGHT // 3, window=b1)


window.mainloop()
