from mem_dixy.module.os import OS


class Path:
    def __init__(self, path=OS.working_directory(), file=None):
        self.directory = path
        #
        self.path = path
        self.file = file

    def change_directory(self, path):
        self.directory = OS.join_path(self.directory, path)

    def load_folder(self, folder):
        self.path = OS.join_path(self.path, folder)

    def get_path(self):
        return self.directory
