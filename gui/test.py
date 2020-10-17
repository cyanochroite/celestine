import os

path = '.'
path = os.path.abspath(path)

print(path)
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.normpath(path))
print(os.path.normpath('.'))

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))


mypath = os.path.normpath(path)
f = []
for (dirpath, dirnames, filenames) in os.walk(mypath):
    f.extend(filenames)
    break

for (path) in f:
    print("HI " + path)

print(f)

import PIL
from mem_dixy.package.Pillow.Image import Image


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

