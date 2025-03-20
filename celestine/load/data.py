""""""

FUNCTION = "<function"
PYTHON_EXTENSION = ".py"


def clamp(minimum, midterm, maximum):
    """The order of the inputs actually don't matter."""
    return sorted((minimum, midterm, maximum))[1]
