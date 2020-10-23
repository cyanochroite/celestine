import PIL
from mem_dixy.package.Pillow.Image import Image

from mem_dixy.module.os import OS
import os
path = "todo"


def get_directory(path):
    directory = []
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir(follow_symlinks=False):
                directory.append(entry.path)
    return directory


def scan():
    directory = get_directory('.')
    for path in directory:
        directory.extend(get_directory(path))
    return directory


pwd = os.getcwd()
os.chdir(path)
print(scan())
os.chdir(pwd)


pwd = os.getcwd()
os.chdir(path)
print("meow")
print(OS.walk_directory('.'))
os.chdir(pwd)


def scan(path):
    file = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        print("A")
        print(dirpath)
        print("B")
        print(dirnames)
        print("C")
        print(filenames)
        for name in filenames:
            file.append(os.path.join(dirpath, name))


scan("todo")

img = Image.open('file/logo.jpg')

# DateTime
# TimeZoneOffset
# UserComment


class Image():
    @classmethod
    def open(cls, Path):
        fp = Path
        mode = "r"
        return PIL.Image.open(fp, mode)


print(PIL.TiffTags.TagInfo)
print("---------------")
print(PIL.TiffTags.TAGS_V2)
print("---------------")
print(PIL.TiffTags.TAGS)


k = PIL.TiffTags.lookup(306)  # DateTime
k = PIL.TiffTags.lookup(270)  # DateTime

# img.TiffTags("candy")

j = PIL.TiffImagePlugin
j.DATE_TIME = "moo"

print(k)


import pathlib


class Path:
    @classmethod
    def Make(cls, path):
        return pathlib.Path(path)

    @classmethod
    def Join(cls, one, two):
        return one.joinpath(two)


print(Path.Make("hippo\dippo"))
