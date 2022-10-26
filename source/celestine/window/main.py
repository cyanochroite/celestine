import celestine.core.load as load
import celestine.core.os as os

#image = {}
image = []


def execute(session, directory):
    (path, file) = os.walk_directory(directory)
    images = []
    for (filenames) in file:
        (dirpath, name) = filenames
        ext = os.file_extension(name).lower()
        if ext in session.image_format:
            merge = os.join(dirpath, name)
            images.append(merge)
    return images


def setup(session, window):
    global image
    directory = session.directory

    directory = "D:\\file\\"
    directory = "D:\\todo\\"
    directory = "D:\\grid\\"
    images = execute(session, directory)
    for imaged in images:
        image.append(window.image_load(imaged))


def main(session, frame, window):
    global image

    setup(session, window)

    window.label(frame, "Settings",
                 "no puppy. File Explorer using Tkinter").grid(0, 0)
    window.file_dialog(frame, "set", "Settings").grid(0, 1)

    index = 8
    for imaged in image:
        x = index % 4
        y = index // 4
        window.image(frame, F"{x}-{y}", imaged).grid(x, y)
        index += 1
