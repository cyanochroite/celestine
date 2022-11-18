"""Python 3.10"""
from celestine.python import python_3_09 as python


def curses_cursor_input_match(key, curses, mouse_x, mouse_y):
    """Move the cursor."""
    match key:
        case curses.KEY_UP:
            mouse_y -= 1
        case curses.KEY_DOWN:
            mouse_y += 1
        case curses.KEY_LEFT:
            mouse_x -= 1
        case curses.KEY_RIGHT:
            mouse_x += 1
    return (mouse_x, mouse_y)


def string_format(string):
    """Format a string."""
    return python.string_format(string)
