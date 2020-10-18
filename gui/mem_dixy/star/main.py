from mem_dixy.package.Pillow.Image import Image
from mem_dixy.module.hashlib import Hash
from mem_dixy.module.pathlib import Path
from mem_dixy.module.os import OS
from mem_dixy.utility.path import Path as PP

print("setup")


def work(path):
    #save = PP(file="demo.png")
    # save.change_directory("done")
    save_path = Path.Make(".")
    save_file = Path.Make("demo.png")
    save_this = Path.Join(save_path, save_file)

    base = Image.open(path)
    image = Image.from_input("RGB", base.size, 0)
    image.paste(base)
    image.save(save_this, "PNG")

    cypher = Hash.sha3_512(save_this)

    move_path = Path.Make("done")
    move_file = Path.Make(cypher + ".png")
    move_this = Path.Join(move_path, move_file)

    OS.rename(save_this, move_this)


print("scan")

import os

# current
dirr = PP()
dirr.change_directory("todo")
f = OS.filenames(dirr.get_path())

for (path) in f:
    print("convert " + path)
    work(path)

print("done")
