def main(_, frame, window):
    window.label(frame, "title", "Page 0").grid(0, 0)
    window.button(frame, "previous", "Page 1", 1).grid(0, 1)
    window.button(frame, "next", "Page 2", 2).grid(0, 2)
