# https://pillow.readthedocs.io/en/stable/reference/ImageTk.html
import PIL.ImageTk as _ImageTk


class ImageTk():
    @classmethod
    def PhotoImage(cls, image):
        return _ImageTk.PhotoImage(image)
