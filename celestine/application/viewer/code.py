""""""


def find_image(session, directory):
    """"""
    path = directory
    include = session.interface.image_format()
    exclude = []
    files = list(file(path, include, exclude))
    return files


def setup(window):
    """"""
    print("cow")
    directory = window.session.attribute.directory
    images = find_image(window.session, directory)
    grid = window.load("grid")

    items = zip(grid.__iter__(), images)

    for group, image in items:
        (_, item) = group
        item.update(image=image)
