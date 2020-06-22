import os


class mem_image:
    def __init__(self, image):
        self.image = image

    def new_RGB(x, y):
        mode = "RGBA"
        size = (x, y)
        color = (0x00, 0x00, 0x00)
        return mem_image._new(mode, size, color)

    def new_RGBA(x, y):
        mode = "RGBA"
        size = (x, y)
        color = (0x00, 0x00, 0x00, 0x00)
        return mem_image._new(mode, size, color)

    def paste(self, them):
        self.image.paste(them.image)

    def save(self, path, format):
        fp = path.path
        self.image.save(fp, format)

    def image_save(image, path):  # {
        if os.path.isfile(path):  # {
            os.remove(path)
        # }
        with open(path, "wb") as file:  # {
            mem_image.save(file, "PNG", optimize=True)
        # }
    # }

    def file_save(load_file):  # {
        load_path = ".\\"
    #    load_file = "bleach_yachiru0035-1.jpg";
        save_path = ".\\"
        save_file = "demo.png"
        base = image_open(load_path + load_file)
        image = image_new(base.size)
        image.paste(base)
        image_save(image, save_path + save_file)
