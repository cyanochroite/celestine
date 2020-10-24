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


def chdir(path, call):
    cwd = os.getcwd()
    os.chdir(path)
    ring = call()
    os.chdir(cwd)
    return ring


sceen = chdir("todo", scan)
print(sceen)

meow = chdir("done", OS.walk_directory)
print(meow)


chdir("done", OS.walk_directory)

pwd = os.getcwd()
os.chdir("done")
for item in sceen:
    os.mkdir(item)

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


from mem_dixy.package.Pillow.Image import Image
from mem_dixy.module.hashlib import Hash
from mem_dixy.module.os import OS
from mem_dixy.module.os import Path


def skip():
    print("setup")

    save_this = Path(file="demo.png").get_file()

    load_this = "todo/todo.png"
    save_this = "a/b/done.png"

    base = Image.open(load_this)
    image = Image.from_input("RGB", base.size, 0)
    image.paste(base)
    image.save(save_this, "PNG")
