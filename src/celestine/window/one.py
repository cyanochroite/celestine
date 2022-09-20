def main(_, frame, window):
    window.label(frame, "title", "Page 1").grid(0, 0)
    window.button(frame, "previous", "Page 0", 0).grid(0, 1)
    window.button(frame, "next", "Page 2", 2).grid(0, 2)
