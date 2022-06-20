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
    self.image("00", image["image1"])
    self.image("01", image["image2"])
    self.label("Settings", "no puppy. File Explorer using Tkinter")
    self.filebox("set", "Settings")


def main(data, window):
    global session
    session = data
    window.run(setup, view)
