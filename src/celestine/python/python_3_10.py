"""Python 3.10"""
from celestine.python import python_3_9 as python


def curses_cursor_input_match(key, curses, x, y):
    """Move the cursor."""
    match key:
        case curses.KEY_UP:
            y -= 1
        case curses.KEY_DOWN:
            y += 1
        case curses.KEY_LEFT:
            x -= 1
        case curses.KEY_RIGHT:
            x += 1
    return (x, y)


def string_format(string):
    """Format a string."""
    return python.string_format(string)
