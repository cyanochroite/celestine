from celestine.application.viewer.core import os


def execute(session, directory):
    (path, file) = os.walk_directory(directory)
    images = []
    for filenames in file:
        (dirpath, name) = filenames
        ext = os.file_extension(name).lower()
        if ext in session.interface.image_format():
            merge = os.join(dirpath, name)
            images.append(merge)
    return images


def setup(window):
    # directory = window.session.directory
    directory = "D:\\file\\"
    directory = "D:\\todo\\"
    directory = "D:\\grid\\"
    image = execute(window.session, directory)
    return image


def window(page):
    image = setup(page)
    with page.line("head") as line:
        line.label("Settings", "no puppy. File Explorer using Tkinter")
    index_y = 0
    limit_y = min(len(image) // 4, 4)
    while index_y < limit_y:
        index_x = 0
        limit_x = min(len(image) - limit_y * index_y, 4)
        with page.line(F"line {index_x}") as line:
            while index_x < limit_x:
                imaged = image[index_y * 4 + index_x]
                line.image(F"{index_x}-{index_y}", imaged)
                index_x += 1
        index_y += 1


def main(_):
    return [
        window,
    ]
