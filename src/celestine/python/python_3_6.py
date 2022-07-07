"""Python 3.6"""


def curses_cursor_input_match(key, curses, x, y):
    """Move the cursor."""
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1
    return (x, y)


def string_format(string):
    """Format a string."""
    return F"{string}"
