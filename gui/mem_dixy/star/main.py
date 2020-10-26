from mem_dixy.package.Pillow.Image import Image
from mem_dixy.module.hashlib import Hash
from mem_dixy.module.os import OS
from mem_dixy.module.os import File

print("setup")


def work(file):

    path = File(file.name, file.path, "todo")
    one = path.join()
    path.root = "done"
    two = path.join()

    Image.convert(one, two)
    path.name = Hash.sha3_512(two) + ".png"
    three = path.join()

    OS.rename(two, three)


print("scan")


(path, file) = OS.chdir("todo", OS.walk_directory)
OS.chdir("done", OS.makedirs, path)
for (f) in file:
    print("convert " + f.name)
    work(f)


print("done")
