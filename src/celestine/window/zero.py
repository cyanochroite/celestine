def main(window):
    with window.frame() as frame:
        with frame.row("head") as row:
            row.label("title", "Page 0")
        with frame.row("body") as row:
            row.button("past", "Page 1", 1)
            row.button("next", "Page 2", 2)
