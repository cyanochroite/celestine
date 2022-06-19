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
