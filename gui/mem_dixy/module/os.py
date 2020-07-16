import os


class OS:
    @classmethod
    def remove(cls, path):
        if os.path.isfile(path):
            os.remove(path)

    @classmethod
    def rename(cls, source, destination):
        if not os.path.isfile(destination):
            os.rename(source, destination)

    def _image_save(image, path):
        if os.path.isfile(path):
            os.remove(path)
        with open(path, "wb") as file:
            image.save(file, "PNG", optimize=True)
