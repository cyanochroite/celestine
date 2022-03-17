# https://pillow.readthedocs.io/en/stable/reference/ImageTk.html
import PIL.ImageTk


class ImageTk():
    @classmethod
    def PhotoImage(cls, image):
        return PIL.ImageTk.PhotoImage(image)
