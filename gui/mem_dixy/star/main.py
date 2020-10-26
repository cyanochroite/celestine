from mem_dixy.package.Pillow.Image import Image
from mem_dixy.module.hashlib import Hash
from mem_dixy.module.os import OS
from mem_dixy.module.os import Path
from mem_dixy.module.os import File

print("setup")


def work(file):

    load_this = OS.join_path("todo", file.full())

    save_this = "demo.png"
    base = Image.open(load_this)
    image = Image.from_input("RGB", base.size, 0)
    image.paste(base)
    image.save(save_this, "PNG")
    cypher = Hash.sha3_512(save_this)

    #move_this = Path("done", cypher + ".png").get_file()
    save = File(cypher + ".png", file.path)
    print(save.full())
    move_this = OS.join_path("done", save.full())

    OS.rename(save_this, move_this)


print("scan")


(path, file) = OS.chdir("todo", OS.walk_directory)
OS.chdir("done", OS.makedirs, path)
for (f) in file:
    print("convert " + f.name)
    work(f)


print("done")
