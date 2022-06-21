import celestine.core.load as load

class main():
    def __init__(self, session):
        self.session = session
        self.image = {}

    def setup(self, window):
        image1 = load.file(self.session, ["file", "anitest.gif"])
        image2 = load.file(self.session, ["file", "test4.gif"])
        self.image["image1"] = window.image_load(image1)
        self.image["image2"] = window.image_load(image2)
    
    
    def view(self, window):
        window.image("00", self.image["image1"])
        window.image("01", self.image["image2"])
        window.label("Settings", "no puppy. File Explorer using Tkinter")
        window.filebox("set", "Settings")
