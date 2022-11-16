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
    with page.line("body") as line:
        index = 8
        for imaged in image:
            x = index % 4
            y = index // 4
            line.image(F"{x}-{y}", imaged)
            index += 1


def main(_):
    return [
        window,
    ]
