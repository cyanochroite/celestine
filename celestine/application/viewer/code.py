""""""
from celestine.load.many import file


def find_image(this, directory):
    """"""
    path = directory
    include = this.window.extension()
    exclude = []
    files = list(file(path, include, exclude))
    return files


def setup(*, this, window, **star):
    """"""
    print("cow")
    directory = this.attribute.directory
    images = find_image(this, directory)
    grid = window.load("grid")

    items = zip(grid.__iter__(), images)

    for group, image in items:
        (_, item) = group
        item.update(this=this, image=image)
