from celestine.core import os


def execute(session, directory):
    (path, file) = os.walk_directory(directory)
    images = []
    for filenames in file:
        (dirpath, name) = filenames
        ext = os.file_extension(name).lower()
        if ext in session.image_format:
            merge = os.join(dirpath, name)
            images.append(merge)
    return images


def setup(window):
    directory = window.session.directory
    directory = "D:\\file\\"
    directory = "D:\\todo\\"
    directory = "D:\\grid\\"
    image = execute(window.session, directory)
    return image


def main(window):
    image = setup(window)

    with window.frame() as frame:
        with frame.row("head") as row:
            row.label("Settings", "no puppy. File Explorer using Tkinter")
            #row.file_dialog("set", "Settings")

        with frame.row("body") as row:
            index = 8
            for imaged in image:
                x = index % 4
                y = index // 4
                row.image(F"{x}-{y}", imaged)
                index += 1


