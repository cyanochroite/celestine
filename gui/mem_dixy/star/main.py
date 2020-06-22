from mem_dixy.Pillow.Image import Image
from mem_dixy.star.mem_hash import mem_hash
from mem_dixy.star.mem_image import mem_image
from mem_dixy.star.mem_path import mem_path

print("setup")

load_path = ".\\"
load_file = "todo.png"
load_this = mem_path(load_path + load_file)
save_path = ".\\"
save_file = "demo.png"
save_this = mem_path(save_path + save_file)

print("scan")

base = mem_image(Image.from_path(load_this))
image = mem_image(Image.from_input("RGB", base.image.size, 0))
image.paste(base)
image.save(save_this, "PNG")

#os_rename(save_path + save_file, save_path)

print("done")

