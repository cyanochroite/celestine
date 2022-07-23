"""Python 3.6"""


def curses_cursor_input_match(key, curses, mouse_x, mouse_y):
    """Move the cursor."""
    if key == curses.KEY_UP:
        mouse_y -= 1
    if key == curses.KEY_DOWN:
        mouse_y += 1
    if key == curses.KEY_LEFT:
        mouse_x -= 1
    if key == curses.KEY_RIGHT:
        mouse_x += 1
    return (mouse_x, mouse_y)


def string_format(string):
    """Format a string."""
    return F"{string}"
