import os


class mem_path:
    def __init__(self, path):
        self.path = path

    def remove(path):
        if os.path.isfile(path):
            os.remove(path)

    def rename(open_spot, save_path):
        save_spot = save_path + file_cypher(open_spot) + ".png"
        if not os.path.isfile(save_spot):
            os.rename(open_spot, save_spot)

    def image_save(image, path):  # {
        if os.path.isfile(path):  # {
            os.remove(path)
        # }
        with open(path, "wb") as file:  # {
            image.save(file, "PNG", optimize=True)
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
        os_rename(save_path + save_file, save_path)


