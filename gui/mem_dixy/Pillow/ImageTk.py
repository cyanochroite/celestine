import PIL.ImageTk


def PhotoImage(name):
    image = PIL.Image.open(name)
    photo = PIL.ImageTk.PhotoImage(image)
    return photo
