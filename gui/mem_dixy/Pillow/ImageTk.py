import PIL.ImageTk


class ImageTk():
    @classmethod
    def PhotoImage(cls, image):
        return PIL.ImageTk.PhotoImage(image)
