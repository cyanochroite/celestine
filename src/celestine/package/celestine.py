"""Package celestine."""


class Window():
    def __init__(self):
        self.item = {}

    def file_dialog(self, tag, bind):
        pass

    def file_dialog_load(self, tag):
        pass

    def image(self, tag, image):
        pass

    def image_load(self, file):
        pass

    def label(self, tag, text):
        pass

    def run(self, app):
        print("Hello user.")
        print("Try '-h' option.")
