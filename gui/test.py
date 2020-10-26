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
