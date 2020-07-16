from mem_dixy.Pillow.Image import Image
from mem_dixy.star.mem_hash import mem_hash
from mem_dixy.star.mem_image import mem_image
from mem_dixy.star.Path import Path

print("setup")

load_path = Path.Make(".")
load_file = Path.Make("todo.png")
load_this = Path.Join(load_path, load_file)
save_path = Path.Make(".")
save_file = Path.Make("demo.png")
save_this = Path.Join(save_path, save_file)

print("scan")

base = mem_image(Image.open(load_this))
image = mem_image(Image.from_input("RGB", base.image.size, 0))
image.paste(base)
image.save(save_this, "PNG")

#os_rename(save_path + save_file, save_path)

print("done")

