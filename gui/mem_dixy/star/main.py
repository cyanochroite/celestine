from mem_dixy.package.Pillow.Image import Image
from mem_dixy.module.hashlib import Hash
from mem_dixy.module.os import OS
from mem_dixy.module.os import Path

print("setup")


def work(load_this):
    save_this = Path(file="demo.png").get_file()

    base = Image.open(load_this)
    image = Image.from_input("RGB", base.size, 0)
    image.paste(base)
    image.save(save_this, "PNG")

    cypher = Hash.sha3_512(save_this)

    move_this = Path("done", cypher + ".png").get_file()

    OS.rename(save_this, move_this)


print("scan")

import os

# current
dirr = Path()
dirr.change_directory("todo")
f = OS.filenames(dirr.get_path())

for (path) in f:
    print("convert " + path)
    work(path)

print("done")
