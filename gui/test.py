import PIL
from mem_dixy.package.Pillow.Image import Image

import os
path = "todo"


def scan(path):
    os.chdir(path)
    todo = []
    done = []
    todo.append('.')
    for derp in todo:
        with os.scandir(derp) as entries:
            for entry in entries:
                if entry.is_dir(follow_symlinks=False):
                    todo.append(entry.path)
                    done.append(entry.name)
    os.chdir('..')
    return (todo, done)


def scan2(path):
    directory = []
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir(follow_symlinks=False):
                directory.append((entry.path, entry.name))
    return directory


print(scan(path))


def join(dirpath, dirname):
    return os.path.join(dirpath, dirname)


def dirjoin(dirpath, dirnames):
    dirpaths = []
    for dirname in dirnames:
        dirpaths.append(os.path.join(dirpath, dirname))
    return dirpaths


def dirwalk(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        return dirnames
    return []


eat = dirwalk(path)
print(eat)
for food in eat:
    now = dirwalk(food)
    print(now)


def walky(path):
    pwd = os.getcwd()
    os.chdir(path)

    derp = []
    magic_path = ""
    for (dirpath, dirnames, filenames) in os.walk('.'):
        for name in dirnames:
            join = os.path.join(dirpath, name)
            derp.append(join)
    os.chdir(pwd)
    return derp


def walk(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        return (dirnames, filenames)
    return ([], [])


(pie, toad) = walk("todo")
print(pie)
print(toad)


meow = walky("todo")
print("meow")
print(meow)


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
