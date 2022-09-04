def setup(session):
    pass


def view(session):
    window = session.task

    window.label("title", "Startpage")
    window.button("title", "Page 1")
    window.button("title", "Page 2")
