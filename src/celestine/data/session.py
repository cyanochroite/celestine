import configparser


def make(parent_directory):
    session = configparser.ConfigParser()

    session.add_section("Application")
    session.set("Application", "name", "celestine")
    session.set("Application", "directory", parent_directory)

    with open("celestine.ini", "w") as file:
        session.write(file)

    session.read("celestine.ini")

    return session



PYTHON = "python"
VERSION = "version"
APPLICATION = "Application"
DIRECTORY = "directory"

class Session():
    def __init__(self, parent_directory):
        self.session = configparser.ConfigParser()
        self.session.read("celestine.ini")

        self.session.add_section(APPLICATION)
        self.session.set(APPLICATION, DIRECTORY, parent_directory)

        self.session.add_section(VERSION)
        self.session.set(VERSION, PYTHON, "3.10") # need to calculate this

    @property
    def python(self):
        return float(self.session[VERSION][PYTHON])

    @property
    def directory(self):
        return self.session[APPLICATION][DIRECTORY]
