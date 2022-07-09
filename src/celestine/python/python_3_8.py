"""Python 3.8"""
from celestine.python import python_3_7 as python


def curses_cursor_input_match(key, curses, x, y):
    """Move the cursor."""
    return python.curses_cursor_input_match(key, curses, x, y)


def string_format(string):
    """Format a string."""
    return python.string_format(string)
