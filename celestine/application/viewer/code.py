""""""
from celestine.load.many import file


def find_image(session, directory):
    """"""
    path = directory
    include = session.window.extension()
    exclude = []
    files = list(file(path, include, exclude))
    return files


def setup(*, session, window, **star):
    """"""
    print("cow")
    directory = session.attribute.directory
    images = find_image(session, directory)
    grid = window.load("grid")

    items = zip(grid.__iter__(), images)

    for group, image in items:
        (_, item) = group
        item.update(session=session, image=image)
