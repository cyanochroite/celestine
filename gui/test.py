import PIL
from mem_dixy.package.Pillow.Image import Image

from mem_dixy.module.os import OS
import os


def chdir(path, call, *args):
    cwd = os.getcwd()
    os.chdir(path)
    ring = call(*args)
    os.chdir(cwd)
    return ring


meow = chdir("todo", OS.walk_directory, '.')
print(meow)


def Delegate(call,
             _0=None,
             _1=None,
             _2=None,
             _3=None,
             _4=None,
             _5=None,
             _6=None,
             _7=None,
             _8=None,
             _9=None,
             _A=None,
             _B=None,
             _C=None,
             _D=None,
             _E=None,
             _F=None
             ):
    if _0 is None:
        return call()
    if _1 is None:
        return call(_0)
    if _2 is None:
        return call(_0, _1)
    if _3 is None:
        return call(_0, _1, _2)
    if _4 is None:
        return call(_0, _1, _2, _3)
    if _5 is None:
        return call(_0, _1, _2, _3, _4)
    if _6 is None:
        return call(_0, _1, _2, _3, _4, _5)
    if _7 is None:
        return call(_0, _1, _2, _3, _4, _5, _6)
    if _8 is None:
        return call(_0, _1, _2, _3, _4, _5, _6, _7)
    if _9 is None:
        return call(_0, _1, _2, _3, _4, _5, _6, _7, _8, _9)
    if _A is None:
        return call(_0, _1, _2, _3, _4, _5, _6, _7, _8, _9, _A)
    if _B is None:
        return call(_0, _1, _2, _3, _4, _5, _6, _7, _8, _9, _A, _B)
    if _C is None:
        return call(_0, _1, _2, _3, _4, _5, _6, _7, _8, _9, _A, _B, _C)
    if _D is None:
        return call(_0, _1, _2, _3, _4, _5, _6, _7, _8, _9, _A, _B, _C, _D)
    if _E is None:
        return call(_0, _1, _2, _3, _4, _5, _6, _7, _8, _9, _A, _B, _C, _D, _E)
    return call(_0, _1, _2, _3, _4, _5, _6, _7, _8, _9, _A, _B, _C, _D, _E, _F)


def Delegate(call, **kw):
    print(kw)
    call(kw)


#Delegate(OS.makedirs, kite=meow)

chdir("done", OS.makedirs, meow)


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
