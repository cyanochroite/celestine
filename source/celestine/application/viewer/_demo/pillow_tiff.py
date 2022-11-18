import sys
sys.path.insert(1, '../src/')

import PIL
from package.pillow.Image import Image


img = Image.open('D:/file/logo.jpg')

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
