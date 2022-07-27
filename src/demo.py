import os.path
CELESTINE = "celestine"
FULL_STOP = "."

def module2(*paths):
    """Load an internal module from anywhere in the application."""
    iterable = [CELESTINE, *paths]
    name = FULL_STOP.join(iterable)
    file = __import__(name)
    for path in paths:
        file = getattr(file, path)
    return file


def module1(*paths):
    """Load an internal module from anywhere in the application."""
    iterable = [CELESTINE] + list(paths)
    name = FULL_STOP.join(iterable)
    item = __import__(name)
    for path in paths:
        item = getattr(item, path)
    return item


def file(*paths):
    """Load a file from absolute path."""
    path = os.path.join(*paths)
    return path

print(module1("language", "english"))
print(module2("language", "english"))

image1 = file("directory", "file", "anitest.gif")
image2 = file("directory", "file", "test4.gif")

print(image1)
print(image2)