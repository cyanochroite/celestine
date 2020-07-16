import os


class Path:
    def __init__(self, path):
        self.path = path

    def remove(path):
        if os.path.isfile(path):
            os.remove(path)

    def rename(open_spot, save_path):
        save_spot = save_path + file_cypher(open_spot) + ".png"
        if not os.path.isfile(save_spot):
            os.rename(open_spot, save_spot)

    def image_save(image, path):
        if os.path.isfile(path):
            os.remove(path)
        with open(path, "wb") as file:
            image.save(file, "PNG", optimize=True)

