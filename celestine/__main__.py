import itertools


import hashlib
from file import lzma
import more_itertools
import random
import base64
import PIL.Image


path = "D:\\OneDrive\\Pictures\\Doom\\Doom Screenshot 2020.01.16 - 09.52.58.59.png"
# path = "D:\\file\\color.png"
path = "D:\\file\\test0.jpg"
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


text = []
for index in range(0x2800, 0x2900):
    text.append(chr(index))

text = "".join(text)
print(text)

image = convert(image)
data = image.getdata()
flat = itertools.chain.from_iterable(data)

lzma.save_data("celestine.temp", flat)
data = lzma.load_data("celestine.temp")

can = PIL.Image.frombytes("RGBA", image.size, data)
can.show()

# print(decode(PIL.Image.open('dmtx.png')))




mport sys
import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

md5 = hashlib.md5()
sha1 = hashlib.sha1()

with open(sys.argv[1], 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
        sha1.update(data)

print("MD5: {0}".format(md5.hexdigest()))
print("SHA1: {0}".format(sha1.hexdigest()))
