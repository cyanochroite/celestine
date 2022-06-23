from celestine.package.pillow.Image import Image
from celestine.package.python.hashlib import hashlib
from celestine.package.python.os import os


def main(todo="D:/todo", done="D:/done"):
    (path, file) = os.chdir(todo, os.walk_directory)
    os.chdir(done, os.makedirs, path)
    for item in file:
        root = todo
        (name, path) = item
        print("convert " + name)

        one = os.join(root, path, name)
        root = done
        two = os.join(root, path, name)

        Image.old_png_convert(one, two)
        name = hashlib.sha3_512(two) + ".png"
        three = os.join(root, path, name)

        os.rename(two, three)
