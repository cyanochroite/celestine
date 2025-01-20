#!/usr/bin/env python3
from PIL import Image


def quantizetopalette(silf, palette, dither=False):
    """Convert an RGB or L mode image to use a given P image's palette."""

    silf.load()

    # use palette from reference image
    palette.load()

    colors = 256
    method = Image.Quantize.MEDIANCUT
    kmeans = 0
    # palette: Image | None = None
    dither = Image.Dither.NONE

    return silf.quantize(colors, method, kmeans, palette, dither)


# putpalette() input is a sequence of [r, g, b, r, g, b, ...]
# The data chosen for this particular answer represent
# the four gray values in a game console's palette
palettedata = [0, 0, 0, 102, 102, 102, 176, 176, 176, 255, 255, 255]
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
# Create a palette image whose size does not matter
arbitrary_size = 16, 16
palimage = Image.new('P', arbitrary_size)
palimage.putpalette(palettedata)

# Perform the conversion
oldimage = Image.open("D:\\done\\1unknown.png")
oldimage = oldimage.convert(mode="RGB")
newimage = quantizetopalette(oldimage, palimage, dither=False)
newimage.show()
