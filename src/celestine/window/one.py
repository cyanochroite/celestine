def setup(session):
    pass


def view(session):
    window = session.task
    window.label("Display", "This is another windew. Wow.")
    window.label("Window", "Load the first window.")
    window.file_dialog("set", "Settings")
