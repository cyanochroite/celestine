import itertools


import more_itertools
import random
import base64
import PIL.Image

from pylibdmtx.pylibdmtx import encode, decode

path = "D:\\OneDrive\\Pictures\\Doom\\Doom Screenshot 2020.01.16 - 09.52.58.59.png"
# path = "D:\\file\\color.png"
# path = "D:\\file\\null.jpg"
image = PIL.Image.open(path)


def convert(image):
    """"""
    mode = "RGBA"
    matrix = None
    dither = PIL.Image.Dither.NONE
    palette = PIL.Image.Palette.WEB
    colors = 256
    return image.convert(mode, matrix, dither, palette, colors)

def _encode(iterable):
    """"""
    data = base64.a85encode(bytes(iterable))
    scheme = "Ascii"
    size = "144x144"
    size = None
    return encode(data, scheme, size)

import bz2
import zlib
import gzip
import lzma
import pickle





image = convert(image)
data = image.getdata()
flat = itertools.chain.from_iterable(data)
data = bytes(flat)

with open('no_compression.pickle', 'wb') as f:
    pickle.dump(data, f)

with gzip.open("gzip_test.gz", "wb") as f:
    pickle.dump(data, f)

with bz2.BZ2File('bz2_test.pbz2', 'wb') as f:
    pickle.dump(data, f)

with lzma.open("lzma_test.xz", "wb") as f:
    pickle.dump(data, f)




image = convert(image)
data = image.getdata()
flat = itertools.chain.from_iterable(data)
split = more_itertools.chunked(flat, 1244)
count = 0
for item in split:
    encoded = _encode(item)

    img = PIL.Image.frombytes(
        'RGB', (encoded.width, encoded.height), encoded.pixels)

    img.save(f"dmtx{count}.png")
    count += 1

print(decode(PIL.Image.open('dmtx.png')))


from pylibdmtx.pylibdmtx import decode
from PIL import Image
carwash = decode(Image.open('dmtx0.png'))
print(carwash)
print(carwash[0][0])
print(carwash[0][1])
cat = 0

