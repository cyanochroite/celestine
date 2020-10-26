from mem_dixy.package.Pillow.Image import Image
from mem_dixy.module.hashlib import Hash
from mem_dixy.module.os import OS

print("scan")


(path, file) = OS.chdir("todo", OS.walk_directory)
OS.chdir("done", OS.makedirs, path)
for (item) in file:
    root = "todo"
    (name, path) = item
    print("convert " + name)

    one = OS.join(root, path, name)
    root = "done"
    two = OS.join(root, path, name)

    Image.convert(one, two)
    name = Hash.sha3_512(two) + ".png"
    three = OS.join(root, path, name)

    OS.rename(two, three)

print("done")
