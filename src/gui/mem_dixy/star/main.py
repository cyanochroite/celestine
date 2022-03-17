from mem_dixy.package.pillow.Image import Image
from mem_dixy.package.python.hashlib import Hash
from mem_dixy.package.python.os import OS

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

    Image.old_png_convert(one, two)
    name = Hash.sha3_512(two) + ".png"
    three = OS.join(root, path, name)

    OS.rename(two, three)

print("done")



