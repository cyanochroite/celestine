import celestine.core.load as load
import os

image = {}
application = None


def setup(self):
    image1 = load.file(session, ["file", "anitest.gif"])
    image2 = load.file(session, ["file", "test4.gif"])
    image["image1"] = self.image_load(image1)
    image["image2"] = self.image_load(image2)


def view(self):
    self.label_add(image["image1"])
    self.label_add(image["image2"])


def main(data, window):
    global session
    session = data
    window.run(setup, view)
