def main(window):
    with window.frame() as frame:
        with frame.row("head") as row:
            row.label("title", "Page 1")
        with frame.row("body") as row:
            row.button("past", "Page 0", 0)
            row.button("next", "Page 2", 2)
