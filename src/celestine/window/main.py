import celestine.core.load as load

image = {}

def setup(session):
    global image
    window = session.application
    directory =  session.asset
    image1 = load.path(directory, "file", "anitest.gif")
    image2 = load.path(directory, "file", "test4.gif")
    image["image1"] = window.image_load(image1)
    image["image2"] = window.image_load(image2)


def view(session):
    global image
    window = session.application
    window.image("00", image["image1"])
    window.image("01", image["image2"])
    window.label("Settings", "no puppy. File Explorer using Tkinter")
    window.file_dialog("set", "Settings")
