from mem_dixy.package.Pillow.Image import Image
from mem_dixy.module.hashlib import Hash
from mem_dixy.module.pathlib import Path
from mem_dixy.module.os import OS

print("setup")


def work(path):
    load_path = Path.Make("todo")
    load_file = Path.Make(path)
    load_this = Path.Join(load_path, load_file)

    save_path = Path.Make(".")
    save_file = Path.Make("demo.png")
    save_this = Path.Join(save_path, save_file)

    base = Image.open(load_this)
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


one = Path.Make(os.path.abspath("."))
two = Path.Make("todo")
mypath = Path.Join(one, two)
print(mypath)
f = []
for (dirpath, dirnames, filenames) in os.walk(mypath):
    f.extend(filenames)
    break

for (path) in f:
    print("convert " + path)
    work(path)

print("done")

