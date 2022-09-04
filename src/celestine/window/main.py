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


def setup(session):
    global image
    window = session.task
    directory = session.directory

    directory = "D:\\file\\"
    directory = "D:\\todo\\"
    images = execute(session, directory)
    for imaged in images:
        image.append(window.image_load(imaged))


def main(session, frame):
    global image

    window = session.task
    setup(session)

    for imaged in image:
        window.image(frame, "00", imaged)

    window.label(frame, "Settings", "no puppy. File Explorer using Tkinter")
    window.file_dialog(frame, "set", "Settings")
