import os

image = {}
root = ""


def setup(self):
    image["image1"] = self.image_load(
        os.path.join(root, "celestine", "file", "anitest.gif")
    )
    image["image2"] = self.image_load(
        os.path.join(root, "celestine", "file", "test4.gif")
    )


def view(self):
    self.label_add(image["image1"])
    self.label_add(image["image2"])


def main(directory, window):
    global root
    root = directory
    window.run(setup, view)
