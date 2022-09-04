def main(session, frame):
    window = session.task
    window.label(frame, "title", "Page 2")
    window.button(frame, "title", "Page 1")
    window.button(frame, "title", "Page 0")
