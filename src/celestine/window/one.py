def main(session, frame):
    window = session.task
    window.label(frame, "title", "Page 1")
    window.button(frame, "previous", "Page 0")
    window.button(frame, "next", "Page 2")
