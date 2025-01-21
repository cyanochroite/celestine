import PIL
from PIL import Image, ImagePalette

import PIL
import PIL.Image


size = 1024
wide = size
tall = size
image = PIL.Image.new("RGB", (wide, tall))


for y in range(tall):
    for x in range(wide):
        xx = x // 4
        yy = y // 4
        boost = 32
        zz = (xx // boost) * boost
        image.putpixel((x, y), (zz, zz, zz))

# image = image.convert(mode="1", dither=PIL.Image.Dither.NONE)
image.show()


image = PIL.Image.new("RGB", (1024, 1024))


for y in range(1024):
    for x in range(1024):
        image.putpixel((x, y), (x // 4, y // 4, 0))

image = image.convert(mode="1", dither=PIL.Image.Dither.NONE)
image.show()


palettedata = []
for index in range(128):
    array = [index * 2, index * 2, index * 2]
    palettedata.extend(array)
# Fill the entire palette so that no entries in Pillow's
# default palette for P images can interfere with conversion
NUM_ENTRIES_IN_PILLOW_PALETTE = 128
num_bands = len("RGB")
num_entries_in_palettedata = len(palettedata) // num_bands
palettedata.extend(
    palettedata[:num_bands]
    * (NUM_ENTRIES_IN_PILLOW_PALETTE - num_entries_in_palettedata)
)

mode = "P"
size = (16, 16)
color = 0
palimage = PIL.Image.new(mode, size, color)


data = palettedata
rawmode = "RGB"
palimage.putpalette(data, rawmode)


# palimage = ImagePalette.ImagePalette(palettedata)

# Perform the conversion
oldimage = Image.open("D:\\done\\1unknown.png")
oldimage = oldimage.convert(mode="RGB")


#


newimage = oldimage.quantize(palette=palimage)
newimage.show()
