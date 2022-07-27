import celestine.core.load as load

class main():
    def __init__(self, session):
        self.session = session
        self.image = {}

    def setup(self):
        window = self.session.application
        directory =  self.session.asset
        image1 = load.path(directory, "file", "anitest.gif")
        image2 = load.path(directory, "file", "test4.gif")
        self.image["image1"] = window.image_load(image1)
        self.image["image2"] = window.image_load(image2)
    
    
    def view(self):
        window = self.session.application
        window.image("00", self.image["image1"])
        window.image("01", self.image["image2"])
        window.label("Settings", "no puppy. File Explorer using Tkinter")
        window.file_dialog("set", "Settings")
